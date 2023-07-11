# How to build a Datenzwerg

!!! warning
    
    The Datenzwerg was developed for the [CCCamp23](https://events.ccc.de/camp/2023/infos/). Hardware, firmware and models were designed for a specific purpose and a specific deployment duration and might not be suitable for other use cases. The Datenzwerg is provided as-is without any warranty, plans to improve or fix it or any other support. If you want to build your own Datenzwerg, you are on your own.

## Prerequisites

Building a Datenzwerg requires some soldering and 3D printing skills.

The firmware provided with the Datenzwerg requires you to provide it with credentials for an existing WiFi network (SSID and password) and also access to an [InfluxDB2](https://influxdb.com) instance (host, port, organization id, bucket name and write-enabled access token). You will need to provide these credentials in a file called `secrets.yaml` in the `firmware` directory. A template for this file is provided in `firmware/secrets-template.yaml`.

## Parts

### Electronics

To build your own Datenzwerg, you will need the following parts:

- 1x D1 mini or compatible ESP8266 board with pin headers
- 1x ADS1115 or compatible I2C 16-bit ADC on a breakout board and with pin headers
- 1x BME280 or compatible I2C temperature, humidity and pressure sensor on a breakout board
- 1x basic UV sensitive photoresistor with opamp on a breakout board
- 1x microphone module (TBD, possibly MAX4466) on a breakout board
- 1x 18650 LiPo battery with holder
- 1x TP4065 LiPo charger module
- 1x 5V boost converter module
- 3x male 3-pin JST connectors and female cables
- 1x male 4-pin JST connector and female cable
- some perfboard to solder everything together on

### Gnome body

If you want to put the Datenzwerg into its gnome body, you will also need:

- 1x 3D printed gnome body top (see `models` directory in the GitHub repository)
- 1x 3D printed gnome body bottom (see `models` directory in the GitHub repository)
- 6x 6x1mm neodymium magnets
- superglue

!!! note

    It is strongly recommended to print the gnome body with a 0.6mm nozzle and 0.4mm layer height. The model is designed for this combination and might not work with other nozzle sizes or layer heights.

## Assembly

### Mainboard

TODO

### Sensors

TODO

### Power supply

TODO

### Gnome body

Using superglue, glue the magnets into the holes in the gnome body bottom. Make sure the polarity is correct, i.e. the magnets attract each other when the gnome body top is placed on the bottom. The magnets should be flush with the surface of the gnome body bottom.

## Flashing the firmware

Make sure the power is disconnected from the Datenzwerg's mainboard. Unplug the D1 mini from the mainboard and connect it to your computer via USB.

Install Python 3.11. Check out the [GitHub repository]() and therein run 

1. `python -m venv venv`
2. `source venv/bin/activate`
3. `pip install -r requirements.txt`

This will install all dependencies needed to build the firmware and the documentation into a virtual environment and activate it.

Then, navigate to the `firmware` directory. Copy `secrets-template.yaml` to `secrets.yaml` and fill in your WiFi and InfluxDB2 credentials. Then run

```
esphome -s name <gnome> datenzwerg.yaml run
```

to compile and flash the firmware for your gnome named `<gnome>` (e.g. if you want to flash the firmware for the gnome named `zwerg`, run `esphome -s name zwerg datenzwerg.yaml run`).

Plug the D1 mini back into the mainboard and reconnect the power. It should connect to your WiFi and start sending data to the configured InfluxDB.
