import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import sensor, voltage_sampler
from esphome.const import (
    CONF_SENSOR,
    DEVICE_CLASS_SOUND_PRESSURE,
    STATE_CLASS_MEASUREMENT,
    UNIT_DECIBEL,
)

AUTO_LOAD = ["voltage_sampler"]
CODEOWNERS = ["@foosel"]

CONF_SAMPLE_DURATION = "sample_duration"
CONF_AMP_GAIN = "amp_gain"
CONF_MIC_SENSITIVITY = "mic_sensitivity"

sound_pressure_ns = cg.esphome_ns.namespace("sound_pressure")
SoundPressureSensor = sound_pressure_ns.class_(
    "SoundPressureSensor",
    sensor.Sensor, cg.PollingComponent
)

CONFIG_SCHEMA = (
    sensor.sensor_schema(
        SoundPressureSensor,
        unit_of_measurement=UNIT_DECIBEL,
        accuracy_decimals=2,
        device_class=DEVICE_CLASS_SOUND_PRESSURE,
        state_class=STATE_CLASS_MEASUREMENT,
    )
    .extend(
        {
            cv.Required(
                CONF_SENSOR
            ): cv.use_id(voltage_sampler.VoltageSampler),
            cv.Optional(
                CONF_SAMPLE_DURATION, default="250ms"
            ): cv.positive_time_period_milliseconds,
            cv.Optional(
                CONF_AMP_GAIN, default=0.0
            ): cv.float_range(min=0.0),
            cv.Optional(
                CONF_MIC_SENSITIVITY, default=0
            ): cv.int_range(max=0),
        }
    )
    .extend(cv.polling_component_schema("60s"))
)


async def to_code(config):
    var = await sensor.new_sensor(config)
    await cg.register_component(var, config)

    sens = await cg.get_variable(config[CONF_SENSOR])
    cg.add(var.set_source(sens))
    cg.add(var.set_sample_duration(config[CONF_SAMPLE_DURATION]))
    cg.add(var.set_amp_gain(config[CONF_AMP_GAIN]))
    cg.add(var.set_mic_sensitivity(config[CONF_MIC_SENSITIVITY]))

    cg.add_global(sound_pressure_ns.using)
