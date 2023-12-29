---
description: "Der Datenzwerg ist ein Gartenzwerg mit einer Mission: Umweltdaten zu sammeln und öffentlich zugänglich zu machen."
---

# Der Datenzwerg

![Datenzwerg Logo](assets/images/logo.png){: class="logo" :}

!!! tip "Datenzwerg @ 37c3"

    Du bist auf dem 37c3 und über einen der Datenzwerge gestolpert? Super! Hier sind ein paar Links für dich:

    - [Was ist der Datenzwerg?](#was-ist-der-datenzwerg)
    - [FAQ](#faq)
    - [Schicke Dashboards auf grafana.datagnome.de](https://grafana.datagnome.de)
    
    Du kannst uns erreichen unter **DECT 3962 (DZOC)**.

    Und falls du dich wunderst, wo sich welcher Datenzwerg befindet, hier eine kurze Übersicht. Ein Klick auf den Namen bringt dich zum jeweiligen Dashboard:

    | Datenzwerg | Location | Status |
    | ---------- | -------- | ------ |
    | [Bashful](https://grafana.datagnome.de/d/f17a6449-84ed-4733-b982-21c0d480c42a/overview?orgId=1&refresh=15m&var-zwerg=Bashful&theme=dark) | NOC Helpdesk | Deployed |
    | [Dopey](https://grafana.datagnome.de/d/f17a6449-84ed-4733-b982-21c0d480c42a/overview?orgId=1&refresh=15m&var-zwerg=Dopey&theme=dark) | DDOS Bar | Deployed |
    | [Grumpy](https://grafana.datagnome.de/d/f17a6449-84ed-4733-b982-21c0d480c42a/overview?orgId=1&refresh=15m&var-zwerg=Grumpy&theme=dark) | Hall Z | Deployed |
    | [Happy](https://grafana.datagnome.de/d/f17a6449-84ed-4733-b982-21c0d480c42a/overview?orgId=1&refresh=15m&var-zwerg=Happy&theme=dark) | Hall G | Deployed |
    | [Hefty](https://grafana.datagnome.de/d/f17a6449-84ed-4733-b982-21c0d480c42a/overview?orgId=1&refresh=15m&var-zwerg=Hefty&theme=dark) | Jugend Assembly | Deployed |
    | [Kinky](https://grafana.datagnome.de/d/f17a6449-84ed-4733-b982-21c0d480c42a/overview?orgId=1&refresh=15m&var-zwerg=Kinky&theme=dark) | Flower Assembly | Deployed |
    | [Moopsy](https://grafana.datagnome.de/d/f17a6449-84ed-4733-b982-21c0d480c42a/overview?orgId=1&refresh=15m&var-zwerg=Moopsy&theme=dark) | Lounge | Deployed |
    | [Nerdy](https://grafana.datagnome.de/d/f17a6449-84ed-4733-b982-21c0d480c42a/overview?orgId=1&refresh=15m&var-zwerg=Nerdy&theme=dark)  | Telnet Assembly | Deployed |
    | [Sleepy](https://grafana.datagnome.de/d/f17a6449-84ed-4733-b982-21c0d480c42a/overview?orgId=1&refresh=15m&var-zwerg=Sleepy&theme=dark) | POC | Deployed |
    | [Sneezy](https://grafana.datagnome.de/d/f17a6449-84ed-4733-b982-21c0d480c42a/overview?orgId=1&refresh=15m&var-zwerg=Sneezy&theme=dark) | Hall E | Deployed |

## Was ist der Datenzwerg?

Der Datenzwerg ist ein Gartenzwerg mit einer Mission: Umweltdaten zu sammeln und öffentlich zugänglich zu machen.

Ursprünglich wurde er für das [Chaos Communication Camp 2023](https://events.ccc.de/camp/2023/infos/) entwickelt, 
wo wir ([@romses](https://chaos.social/@romses) und [@foosel](https://chaos.social/@foosel)) eine kleine Armee 
von 10 Datenzwergen über das Camp-Gelände verteilt hatten: Happy, Doc, Grumpy, Dopey, Bashful, Sleepy, Sneezy, 
Nerdy, Kinky und Hefty[^1].

Wenn alles klappt, werden die Datenzwerge auf dem [37c3](https://events.ccc.de/congress/2023/infos/index.html) wieder zum Einsatz kommen.

Der Datenzwerg besteht aus einem 3D-gedruckten Gartenzwerg, einer eigenen Platine mit einem ESP8266 D1 Mini Mikrocontroller, einem BME280, SGP30, UV- und Schallsensor und optional einer 18650 Batterie. Er wird von [ESPHome](https://esphome.io/) betrieben und sendet seine Daten an eine [InfluxDB](https://www.influxdata.com/) Instanz. Die Firmware zeichnet derzeit Temperatur, relative und absolute Luftfeuchtigkeit, Luftdruck, Taupunkt, UV-Index eCO2, TVOC und Schalldruck auf.

Wir haben ChatGPT gebeten, den Datenzwerg für uns zu beschreiben[^2] und das ist dabei herausgekommen:

> Willkommen in der Welt des Datenzwergs, einem bezaubernden Gartenzwerg mit einem technologischen Twist!
> Diese entzückende kleine Kreatur mag wie eine gewöhnliche Gartendekoration aussehen,
> aber sie birgt eine geheime Mission, die so faszinierend wie wichtig ist.
> Der Datenzwerg ist auf einer Mission, Umweltdaten zu sammeln und sie für das Wohl aller öffentlich zugänglich zu machen.
>
> [...]
>
> Durch die Nutzung seines einzigartigen Standpunktes in Gärten und Außenbereichen
> bietet der Datenzwerg eine beispiellose Perspektive auf die Umwelt um uns herum.
>
> Alle von diesen umweltfreundlichen Wächtern gesammelten Daten werden frei
> über eine intuitive Online-Plattform zur Verfügung gestellt.
>
> [...]
>
> Auf dem kommenden Chaos Communication Camp freuen wir uns, den Datenzwerg einer
> breiteren Öffentlichkeit von Technikbegeisterten, Hackern und Umweltaktivisten vorzustellen.
> Diese außergewöhnliche Verbindung von Natur und Technologie zeigt das Potenzial für
> bürgerschaftliches Umweltmonitoring auf.

## Eine kurze Geschichte des Datenzwergs

2023-06-11
: Die Idee des Datenzwergs wird am letzten Tag der [GPN21](https://entropia.de/GPN21) geboren, kurz vor der gemeinsamen 
  Barschicht von [@romses](https://chaos.social/@romses) und [@foosel](https://chaos.social/@foosel). Die ruhigeren 
  Momente der Barschicht sowie die Rückfahrt ins Rhein-Main-Gebiet werden für die Diskussion der Idee genutzt. Romses 
  registriert eine Domain.

2023-06-30
: romses und foosel treffen sich für eine gemeinsame Bastelsession. Die ersten zwei Mainboards werden gebaut. Der Datenzwerg lebt!

2023-07-08
: Eine weitere gemeinsame Bastelsession. Weitere 8 Mainboards werden gebaut. Die Datenzwerg-Armee wächst!

2023-07-19
: Nachdem das Modell fertiggestellt und 60+ Stunden gesamte Druckzeit vergangen sind, sind alle 10 Datenzwerg-Körper gedruckt.

2023-07-23
: Die Grundinfrastruktur geht live. Sensoren beginnen, an die offiziellen Server unter [datagnome.de](https://datagnome.de) zu berichten.

: Alle Datenzwerg-Körper werden für die Installation ihrer Elektronik vorbereitet: Magnete werden eingeklebt, die UV-durchlässigen Scheiben werden installiert und alle Löcher mit Milliput gefüllt.

2023-07-24
: Die Firmware erreicht einen ersten funktionsfähigen Zustand.

2023-07-28
: Alle Zwerge stecken jetzt in ihren Körpern und senden fleißig Daten.

2023-08-04
: Die Webseite erreicht einen ersten vollständigen Zustand in Deutsch und Englisch.

2023-08-09
: Die Daten sind öffentlich via InfluxDB und MQTT zugänglich.

: Es erfolgen letzte Anpassungen der Firmware für das Deployment auf dem Camp.

2023-08-11
: Die Zwerge sind vorübergehend wieder offline. Nächster Halt: CCCamp!

2023-08-15 - 2023-08-19
: Datenzwerg Einsatz auf dem [CCCamp23](https://events.ccc.de/camp/2023/infos/).

2023-08-19
: Die Zwerge haben (fast) alle das Camp verlassen und sind auf dem Weg zurück ins Rhein-Main-Gebiet. Vielen Dank für das rege Interesse!

2023-08-22
: Die Zwerge sind wieder zuhause und werden für zukünftige Einsätze vorbereitet. Der Datenexport from CCCamp ist [im Repository verfügbar](https://github.com/romses/Datenzwerg/tree/main/camp23_data).

2023-08-28
: Die Infrastruktur ist vorerst offline und nur noch diese Webseite und der Sourcecode bleiben verfügbar. Die Datenzwerge gönnen sich eine wohlverdiente Pause.

2023-10-30
: Es geht los mit der 37c3 Edition der Datenzwerge. Der Plan ist es, TVOC Monitoring zur Sensor-Suite hinzuzufügen. Eine neue Platine wurde entworfen, bestellt, und zehn neue Mainboards wurden gelötet.

2023-12-08
: Eine alternative Version des Datenzwergunterteils wurde erstellt, die die Durchführung eines Kabels erlaubt. Zehn neue Unterteile wurden gedruckt und magnetisiert, und erlauben damit den Einsatz von USB oder POE für die Stromversorgung auf dem 37c3. Damit sind die Vorbereitungen der Hardware für den 37c3 abgeschlossen.

2023-12-11
: Die Server-Infstruktur ist wieder am Start und die ersten Datenzwerge senden wieder Daten.

2023-12-26
: Die Datenzwerge sind auf dem 37c3 im Einsatz. Die ersten Daten sind online.

## FAQ

### Was für Daten werden vom Datenzwerg aufgezeichnet?

Der Datenzwerg hat Sensoren, die die folgenden Daten aufzeichnen:

- Temperatur
- Relative Luftfeuchtigkeit
- Luftdruck
- eCO2
- TVOC
- UV-Sensor-Spannung
- Mikrofon-Spannung
- Batteriespannung
- WiFi-Signalstärke

Wir berechnet Taupunkt und absolute Luftfeuchtigkeit aus den Temperatur- und relativen Luftfeuchtigkeitswerten, UV-Index aus der Spannung des UV-Sensors und Schalldruck (Lautstärke) aus der Mikrofonspannung. Die Berechnungen werden in der Firmware durchgeführt.

### Nehmt ihr Audio auf?

Nein. Zwar hat jeder Datenzwerg ein Mikrofon im Inneren, das an den ADC des ESPs angeschlossen ist, wir nutzen es jedoch nur, um alle 5s jeweils 1s an Audiosamples zu loggen, aus denen wir dann die Peak-to-Peak-Spannung und daraus den Schalldruck auf dem Datenzwerg selbst berechnen. Die Abtastrate ist viel zu niedrig und ungleichmäßig, um irgendwelches sinnvolles Audio aufzuzeichnen, und das Rauschen auf der Leitung vs. dem 10-Bit-ADC würde auch für eine schlechte Erfahrung sorgen, wenn das unser Ziel wäre. Wir sind nicht an Audio interessiert, wir sind an Lautstärke interessiert.

### Wie lange hält die Batterie?

In unseren Tests hält ein Datenzwerg zwischen drei und vier Tagen mit einer einzigen Ladung unserer 18650 LiPos, die von 1600mAh bis 2800 mAh reichen. Dies hängt natürlich von der Zellkapazität ab, aber auch von der Temperatur und anderen Umweltfaktoren.

Mit dem TVOC Sensor an Bord reicht eine einzelne 18650 Zelle leider nicht aus.

### Warum sind die Temperaturdaten tagsüber so hoch?

Wir müssen die Zwerge in die direkte Sonne stellen, damit der UV Sensor messen kann. Darüber hinaus sondern der ESP und nun auch der TVOC-Sensor selbst Wärme ab. Wir haben versucht, genug Luftdurchfluss im Zwerg zu erzeugen, leider strahlt das Material sehr stark ab. Von daher sind die Temperaturen, insbesondere bei direkter Sonneneinstrahlung, leider verfälscht.

### Wo kann ich die Daten sehen?

Jeder Datenzwerg sendet seine Daten an eine zentrale, selbst gehostete InfluxDB-Instanz. Die Daten werden dann mit Grafana visualisiert. 

Einige dieser Visualisierungen sowie auch die Zugangsdaten um die Rohdaten selbst abzufragen, sowie Links zu Exports vergangener Veranstaltungen können [hier](./sensors/) gefunden werden.

### Wo finde ich den Sourcecode?

Alles kann in diesem GitHub-Repository gefunden werden: [romses/Datenzwerg](https://github.com/romses/Datenzwerg).

## Medienecho

- Die Datenzwerge waren der Opener des Camp reviews 2023 [media.ccc.de](https://media.ccc.de/v/camp2023-57105-cccamp23_review).
- romses und foosel waren zu Gast beim [Datenleben Podcast](https://www.datenleben.de/index.php/2023/10/14/dl043-perspektiven-auf-data-science/) und haben über die Datenzwerge gesprochen.

## Credits & Danksagung

Der Datenzwerg ist ein Gemeinschaftsprojekt von [@romses](https://chaos.social/@romses) und [@foosel](https://chaos.social/@foosel).

Das Datenzwerg-Logo wurde von D.B. entworfen.

Das Datenzwerg-Modell basiert auf [diesem "Garden Gnome" Modell](https://www.printables.com/model/260908-garden-gnome) von [Sci3D](https://www.printables.com/@Sci3D), das unter CC-BY veröffentlicht ist. Unser Remix kann [hier](https://www.printables.com/model/534875-datenzwerg-enclosure) und natürlich auch [im GitHub Repository](https://github.com/romses/Datenzwerg/tree/main/models) gefunden werden.

Die SCD41 sensoren wurden gesponsort von [@dx@mastodon.social](https://chaos.social/@dx@mastodon.social).

[^1]: Ja, die letzten drei genannten Namen sind nicht canon, und einer von ihnen gehört sogar einem Schlumpf - na und, Chaos ftw!
[^2]: Prompt: 'Write me a text for a website that gives an overview of the "Datenzwerg". The Datenzwerg is a garden gnome that collects environmental data, and makes it publicly available. The Datenzwerg will be presented at the Chaos Communication Camp.'
