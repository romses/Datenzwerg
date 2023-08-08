# Current Datenzwerg data

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

If you are interested in the raw data, connect to our InfluxDB or MQTT (read-only):

  - InfluxDB:
    - Host: `influxdb.datagnome.de`
    - Port: 80
    - Organization: `datagnome`
    - Bucket: `datagnome`
    - Auth token: `5amv72PFZxPmnbUISjntEVxtElDYMhkeofg9Deo1ykO6Zy2XIba_iWPcyxyAp_R0dHsvHm5moE4YBCwxGIEriw==`
  - MQTT:
    - Host: `datagnome.de`
    - Port: 1883
    - User: `cccamp23`
    - Password: `cccamp23`
