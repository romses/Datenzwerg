import logging
import os
import yaml

from esphome import git

from esphome.core import CORE
from esphome.components import text_sensor
import esphome.config_validation as cv
import esphome.codegen as cg
from esphome.const import CONF_ID, ENTITY_CATEGORY_DIAGNOSTIC

_LOGGER = logging.getLogger(__name__)

ICON_SOURCE_BRANCH = "mdi:source-branch"

git_ref_ns = cg.esphome_ns.namespace("git_ref")
git_ref_TextSensor = git_ref_ns.class_(
    "GitRefTextSensor", text_sensor.TextSensor, cg.PollingComponent
)

CONFIG_SCHEMA = (
    text_sensor.text_sensor_schema(
        git_ref_TextSensor,
        entity_category=ENTITY_CATEGORY_DIAGNOSTIC,
        icon=ICON_SOURCE_BRANCH,
    )
    .extend(
        {
            cv.Optional("commit-ish"): cv.string,
            cv.Optional("broken"): cv.string,
            cv.Optional("dirty"): cv.string,
            cv.Optional("unversioned", default="-UNVERSIONED"): cv.string,
            cv.Optional("all", default=False): cv.boolean,
            cv.Optional("tags", default=False): cv.boolean,
            cv.Optional("long", default=False): cv.boolean,
            cv.Optional("abbrev"): cv.positive_int,
        }
    )
    .extend(cv.polling_component_schema("never"))
)


def is_config_versioned():
    CONFIG_DIR = os.path.dirname(os.path.abspath(CORE.config_path))
    GIT_ROOT_DIR = git.run_git_command(
        ["git", "rev-parse", "--show-toplevel"], CONFIG_DIR
    )
    COMMON_PATH = os.path.commonpath([CONFIG_DIR, GIT_ROOT_DIR])
    config_path_trimmed = os.path.relpath(
        os.path.abspath(CORE.config_path), COMMON_PATH
    )
    _LOGGER.debug(
        "Git Root Directory: %s,\n Config Directory: %s,\n Common: %s,\n --> Config relative to Git: %s,\n config_path: %s",
        GIT_ROOT_DIR,
        CONFIG_DIR,
        COMMON_PATH,
        CORE.config_path,
        config_path_trimmed,
    )
    git_ls_files = git.run_git_command(
        ["git", "ls-files", config_path_trimmed], GIT_ROOT_DIR
    )
    return git_ls_files == config_path_trimmed


def get_git_diff(GIT_DIR, cached=False):
    DIFF_COMMAND = ["git", "diff", "--name-only"]
    if cached:
        DIFF_COMMAND.append("--cached")
    _diff = git.run_git_command(DIFF_COMMAND, GIT_DIR).splitlines()
    return _diff


def get_git_diff_file_paths(config):
    CONFIG_DIR = os.path.dirname(os.path.abspath(CORE.config_path))
    GIT_ROOT_DIR = git.run_git_command(
        ["git", "rev-parse", "--show-toplevel"], CONFIG_DIR
    )
    DIFF_PATHS_MERGED = list(
        set().union(get_git_diff(GIT_ROOT_DIR, False), get_git_diff(GIT_ROOT_DIR, True))
    )
    _diffs = [os.path.join(GIT_ROOT_DIR, file) for file in DIFF_PATHS_MERGED]
    return _diffs


def get_config_file_paths(config):
    CONFIG_DIR = os.path.dirname(os.path.abspath(CORE.config_path))
    CONFIG_FILES = [os.path.abspath(CORE.config_path)]

    class Tagged:
        def __init__(self, tag, wrapped):
            self.tag = tag
            self.wrapped = wrapped

        def __repr__(self):
            return f"Tagged({self.tag!r}, {self.wrapped!r})"

    def constructUndefined(self, node):
        if isinstance(node, yaml.nodes.ScalarNode):
            value = self.construct_scalar(node)
        elif isinstance(node, yaml.nodes.SequenceNode):
            value = self.construct_sequence(node)
        elif isinstance(node, yaml.nodes.MappingNode):
            value = self.construct_mapping(node)
        else:
            _LOGGER.warning(f"Unexpected node {node!r}")
        return Tagged(node.tag, value)

    def getLoader():
        loader = yaml.SafeLoader
        loader.add_constructor(None, constructUndefined)
        return loader

    def getYamlData(fname):
        return yaml.load(open(fname, "rb"), Loader=getLoader())

    def genericItems(dict_or_list):
        if isinstance(dict_or_list, dict):
            return dict_or_list.items()
        if isinstance(dict_or_list, list):
            return enumerate(dict_or_list)

    def getTaggedValues(dictionary):
        result = []
        for _, value in genericItems(dictionary):
            if isinstance(value, dict) or isinstance(value, list):
                nested_result = getTaggedValues(value)
                if nested_result:
                    result += nested_result
            elif isinstance(value, Tagged) and value.tag.startswith("!include"):
                if value.tag == "!include":
                    # result.append(value)
                    result.append(value.wrapped)
                else:
                    _LOGGER.warning("Cannot yet handle tag '%s'!", value.tag)
        return result

    def getAllIncludes(fname):
        try:
            data = getYamlData(fname)
            includes = [os.path.join(CONFIG_DIR, f) for f in getTaggedValues(data)]
            return includes
        except FileNotFoundError as err:
            _LOGGER.error("getAllIncludes: %s", err)
            return []

    def getAllNestedConfigs(fname):
        allIncludes = []
        includes = getAllIncludes(fname)
        for subconf in includes:
            nestedIncludes = getAllNestedConfigs(subconf)
            if nestedIncludes:
                allIncludes += nestedIncludes
        allIncludes += includes
        return allIncludes

    def getFullPaths(f):
        fullPath = os.path.join(CONFIG_DIR, f)
        if os.path.isdir(fullPath):
            dir_files = []
            for root, _, files in os.walk(fullPath):
                dir_files += [os.path.join(root, name) for name in files]
            return dir_files
        else:
            return fullPath

    CONFIG_FILES += getAllNestedConfigs(os.path.abspath(CORE.config_path))

    def getAllCppIncludes(fnames):
        cpp_includes = []
        for fname in fnames:
            data = getYamlData(fname)
            includes = data.get("esphome", {}).get("includes", {})
            cpp_includes += [getFullPaths(f) for f in includes]
        return cpp_includes

    def getLocalExternalComponents(fnames):
        external_component_files = []
        for fname in fnames:
            data = getYamlData(fname)
            external_components = data.get("external_components", {})

            def getComponentDir(source):
                if isinstance(source, str):
                    if "://" in source:
                        return None
                    else:
                        return os.path.join(CONFIG_DIR, source)
                elif source.get("type") == "local":
                    return os.path.join(CONFIG_DIR, source.get("path"))
                return None

            for comps in external_components:
                directory = getComponentDir(comps.get("source"))
                if directory:
                    if "all" == comps.get("components"):
                        external_component_files += getFullPaths(directory)
                    else:
                        for comp in comps.get("components"):
                            external_component_files += getFullPaths(
                                os.path.join(directory, comp)
                            )

        _LOGGER.debug("external_component files %s", external_component_files)
        return external_component_files

    cpp_includes = getAllCppIncludes(CONFIG_FILES)
    external_components = getLocalExternalComponents(CONFIG_FILES)
    CONFIG_FILES += cpp_includes
    CONFIG_FILES += external_components

    ## Files to look for in config:
    # - [x] Package includes
    # - [x] esphome: {'includes': ['../Custom/my_macros.h']
    # - [x] local external components

    return CONFIG_FILES


def produce_git_describe(config):
    # Fails when config directory is not a git repo.
    _LOGGER.debug("produce_git_describe: %s", config)
    CONFIG_DIR = os.path.dirname(os.path.abspath(CORE.config_path))
    dirty_postfix = ""

    GIT_ROOT_DIR = git.run_git_command(
        ["git", "rev-parse", "--show-toplevel"], CONFIG_DIR
    )

    COMMAND = ["git", "describe"]

    if config.get("all", False):
        COMMAND.append("--all")
    if config.get("tags", False):
        COMMAND.append("--tags")
    if config.get("long", False):
        COMMAND.append("--long")

    if "abbrev" in config:
        COMMAND.append(f"--abbrev={config['abbrev']}")
    if "broken" in config:
        COMMAND.append(f"--broken={config['broken']}")
    if "commit-ish" in config:
        COMMAND.append(f"{config['commit-ish']}")

    if "dirty" in config:
        # COMMAND.append(f"--dirty={config['dirty']}")
        if is_config_versioned():
            diff_paths = get_git_diff_file_paths(config)
            config_paths = get_config_file_paths(config)
            _LOGGER.info(
                "Checking git Diffs: \n%s\n\nAgainst files in config: \n%s\n",
                diff_paths,
                config_paths,
            )
            for file in config_paths:
                if file in diff_paths:
                    dirty_postfix = config["dirty"]
                    _LOGGER.warning("Config dirty: '%s' has changes", file)
        else:
            _LOGGER.warning("Config File '%s' is unversioned!", CORE.config_path)
            dirty_postfix = config["unversioned"]

    _LOGGER.info("  Command: %s", COMMAND)
    _describe = git.run_git_command(COMMAND, GIT_ROOT_DIR)
    _describe += dirty_postfix
    _LOGGER.info("  GIT Describe result: %s", _describe)

    return _describe


async def to_code(config):
    git_ref_result = produce_git_describe(config)
    var = cg.new_Pvariable(config[CONF_ID], git_ref_result)
    await cg.register_component(var, config)
    await text_sensor.register_text_sensor(var, config)
