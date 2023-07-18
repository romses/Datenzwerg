import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import sensor, voltage_sampler
from esphome.const import (
    CONF_SENSOR,
    DEVICE_CLASS_VOLTAGE,
    STATE_CLASS_MEASUREMENT,
)

AUTO_LOAD = ["voltage_sampler"]
CODEOWNERS = ["@foosel"]

CONF_SAMPLE_DURATION = "sample_duration"
CONF_DC_BIAS = "dc_bias"

rms_ns = cg.esphome_ns.namespace("rms")
RMSSensor = rms_ns.class_(
    "RMSSensor",
    sensor.Sensor, cg.PollingComponent
)

CONFIG_SCHEMA = (
    sensor.sensor_schema(
        RMSSensor,
        unit_of_measurement="Vrms",
        accuracy_decimals=2,
        device_class=DEVICE_CLASS_VOLTAGE,
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
                CONF_DC_BIAS, default=0.0
            ): cv.float_range(min=0.0),
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
    cg.add(var.set_dc_bias(config[CONF_DC_BIAS]))

    cg.add_global(rms_ns.using)
