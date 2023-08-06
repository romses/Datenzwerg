# Aktuelle Datenzwergdaten

## Umgebungsdaten

{% for env in grafana.environment %}
=== "{{ env.name.de }}"
    <iframe src="{{ grafana.base_url }}{{ env.panel }}" class="grafana-iframe"></iframe>
{% endfor %}

## Interne Daten

{% for env in grafana.internal %}
=== "{{ env.name.de }}"
    <iframe src="{{ grafana.base_url }}{{ env.panel }}" class="grafana-iframe"></iframe>
{% endfor %}

Mehr Dashboards sind unter <a href="https://grafana.datagnome.de">grafana.datagnome.de</a> verfügbar

Wenn du an den Rohdaten interessiert bist, verbinde dich einfach auf unsere Datenbank:

| URL        | influxdb.datagnome.de:80 |
| Auth token | 5amv72PFZxPmnbUISjntEVxtElDYMhkeofg9Deo1ykO6Zy2XIba_iWPcyxyAp_R0dHsvHm5moE4YBCwxGIEriw== |