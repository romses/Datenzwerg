# Datenzwerg

## Development

Install Python 3.11. Then

1. `python -m venv venv`
2. `source venv/bin/activate`
3. `pip install -r requirements.txt`

This will install all dependencies for firmware and documentation development into a virtual environment and activate it. To leave the virtual environment, run `deactivate`.

### Firmware

The Datenzwerg firmware is based on [esphome](https://esphome.io/) which gets installed as dependency when running the above setup command.

> [!NOTE]
>
> The firmware currently requires ESPHOME 2025.7.4, as set in the `requirements.txt`. Other versions might cause errors.

To flash your own Datenzwerg, navigate to the `firmware` directory, then

1. Copy `secrets-template.yaml` to `packages/secrets.yaml` and fill in your WiFi and InfluxDB2 credentials.
2. Run `esphome -s name <gnome> run datenzwerg-{psu|battery|sensortest}.yaml` to compile and flash the firmware for your gnome named `<gnome>`.
   - `psu`: firmware optimized for deployment with a power supply; includes uptime, CO2 sensor and MQTT
   - `battery`: firmware optimized for deployment with a battery; disables uptime, CO2 sensor and MQTT but enables deepsleep
   - `sensortest`: firmware for testing all sensors; enables a webserver to check tracking

### Models

The gnome model files are based on https://www.printables.com/model/260908-garden-gnome by [Sci3D](https://www.printables.com/@Sci3D), released under CC-BY.

In the `models` directory, you will find the following files:

  - **Gnome body**
    - `datenzwerg_40p_1.2mm.blend`: Main design file, edit with [Blender](https://blender.org)
    - `datenzwerg_40p_1.2mm_top.stl`: Upper body, electronics compartment
    - `datenzwerg_40p_1.2mm_bottom.stl`: Lower body, feet, mount point
    - `datenzwerg_40p_1.2mm_bottom_poe.stl`: Lower body, feet, mount point, PoE versionA
    - `datenzwerg_logo.svg`: Logo in SVG format
  - **Gnome mounting**
    - `ground-plate-bottom.FCStd`: Ground plate design file, edit with [FreeCAD](https://freecad.org)
    - `ground-plate-bottom.stl`: Ground plate bottom part
  - **Gnome transport L-Boxx**
    - `l-boxx-136-inlay.FCStd`: L-Boxx Inlay design file, edit with [FreeCAD](https://freecad.org)
    - `label-l-boxx.svg`: Label for the L-Boxx
  - **Various labels**
    - `label-2024.svg`: Gnome label for 37c3

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
