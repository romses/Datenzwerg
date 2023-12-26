---
description: "A look at the current Datenzwerg sensor data."
---

# Current Datenzwerg data

<!--
There is currently no current Datenzwerg data. Check again when they are back at an event.
-->

## Environmental data

{% for env in grafana.environment %}
=== "{{ env.name.en }}"
    <iframe src="{{ grafana.base_url }}{{ env.panel }}" class="grafana-iframe"></iframe>
{% endfor %}

## Internal data

{% for env in grafana.internal %}
=== "{{ env.name.en }}"
    <iframe src="{{ grafana.base_url }}{{ env.panel }}" class="grafana-iframe"></iframe>
{% endfor %}

The full set of grafana dashboards are available at <a href="https://grafana.datagnome.de">grafana.datagnome.de</a>

## Raw data

If you are interested in the raw data, connect to our InfluxDB or MQTT (read-only):

  - InfluxDB:
    - Host: `influxdb.datagnome.de`
    - Port: 8086
    - Organization: `datagnome`
    - Bucket: `datagnome`
    - Auth token: `5amv72PFZxPmnbUISjntEVxtElDYMhkeofg9Deo1ykO6Zy2XIba_iWPcyxyAp_R0dHsvHm5moE4YBCwxGIEriw==`
  - MQTT:
    - Host: `mqtt.datagnome.de`
    - Port: 1883
    - User: `readonly`
    - Password: `readonly`

## Datagnome locations @37C3
  - Bashful: NOC Helpdesk
  - Dopey: DDOS Bar
  - Grumpy: Hall Z
  - Happy: Hall G
  - Hefty: Jugend Assembly
  - Moopsy: Hall 1
  - Nerdy: Telnet Assembly
  - UNNAMED: Flower Assembly
  - Sleepy: POC
  - Sneezy: Hall E
  - 

## Exports of past events

You can find the data export of CCCamp23 [on the repo](https://github.com/romses/Datenzwerg/tree/main/exports/cccamp2023).
