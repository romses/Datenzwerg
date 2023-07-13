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
