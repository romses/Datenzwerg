# Datenzwerg

## Development

Install Python 3.11. Then

1. `python -m venv venv`
2. `source venv/bin/activate`
3. `pip install -r requirements.txt`

This will install all dependencies for firmware and documentation development into a virtual environment and activate it. To leave the virtual environment, run `deactivate`.

### Firmware

The Datenzwerg firmware is based on [esphome](https://esphome.io/) which gets installed as dependency when running the above setup command.

To flash your own Datenzwerg, navigate to the `firmware` directory, then

1. Copy `secrets-template.yaml` to `secrets.yaml` and fill in your WiFi and InfluxDB2 credentials.
2. Run `esphome -s name <gnome> run datenzwerg.yaml` to compile and flash the firmware for your gnome named `<gnome>`.

### Models

The gnome model files are based on https://www.printables.com/model/260908-garden-gnome by [Sci3D](https://www.printables.com/@Sci3D), released under CC-BY.

In the `models` directory, you will find the following files:

- `datenzwerg_40p_1.2mm.blend`: Main design file, edit with [Blender](https://blender.org)
- `datenzwerg_40p_1.2mm_top.stl`: Upper body, electronics compartment
- `datenzwerg_40p_1.2mm_bottom.stl`: Lower body, feet, mount point
- `datenzwerg_40p_1.2mm_bottom_poe.stl`: Lower body, feet, mount point, PoE versionA

Additionally you'll find some SVGs for laser cutting foam inserts for L-Boxx cases to store the Datenzwerge in, and some labels and logos.

### Documentation

The documentation is built with [MkDocs](https://www.mkdocs.org/) which gets installed as dependency when running the above setup command. The documentation source files are located in the `docs` directory, the configuration in `mkdocs.yml` in the project root.

To run a live-reload server, run

```
mkdocs serve
```

To build the documentation, run

```
mkdocs build
```
