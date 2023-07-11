# Datenzwerg Firmware

The Datenzwerg Firmware is based on [esphome](https://esphome.io/).

To flash your own Datenzwerg, first install esphome, then

1. Copy `secrets-template.yaml` to `secrets.yaml` and fill in your WiFi and InfluxDB2 credentials.
2. Run `esphome -s name <gnome> firmware.yaml run` to compile and flash the firmware for your gnome named `<gnome>`.
