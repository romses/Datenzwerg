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
