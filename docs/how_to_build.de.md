# Wie man einen Datenzwerg baut

!!! warning
    
    Der Datenzwerg wurde für das [CCCamp23](https://events.ccc.de/camp/2023/infos/) entwickelt. Hardware, Firmware und Modelle wurden für einen bestimmten Zweck und eine bestimmte Nutzungsdauer entwickelt und sind möglicherweise nicht für andere Anwendungsfälle geeignet. Der Datenzwerg wird wie er ist ohne jegliche Garantie, Pläne zur Verbesserung oder Behebung oder andere Unterstützung bereitgestellt. Wenn du deinen eigenen Datenzwerg bauen möchtest, bist du auf dich allein gestellt.

## Voraussetzungen

Einen Datenzwerg zu bauen erfordert etwas Löterfahrung und 3D-Druckkenntnisse.

Die Firmware, die für den Datenzwerg zur Verfügung gestellt wird, erfordert, dass du ihr Zugangsdaten für ein vorhandenes WiFi-Netzwerk (SSID und Passwort) und auch Zugang zu einer [InfluxDB2](https://influxdb.com)-Instanz (Host, Port, Organisations-ID, Bucket-Name und schreibfähiges Zugriffstoken) zur Verfügung stellst. Du musst diese Zugangsdaten in einer Datei namens `secrets.yaml` im Verzeichnis `firmware` angeben. Eine Vorlage für diese Datei findest du in `firmware/secrets-template.yaml`.

## Teile

### Elektronik

Um deinen eigenen Datenzwerg zu bauen, benötigst du folgende Teile:

- 1x D1 mini mit Pinheadern
- 1x ADS1115 I2C 16-bit ADC auf Breakout-Board und Pinheadern
- 1x BME280 I2C Temperatur-, Luftfeuchtigkeits- und Luftdrucksensor auf Breakout-Board
- 1x UV sensitiver Photoresistor mit Opamp auf einem Breakout-Board
- 1x Mikrofonmodul (TBD, vermutlich MAX4466) auf Breakout-Board
- 1x 18650 LiPo mit Halter
- 1x TP4065 LiPo Lademodul
- 1x 5V Boost-Converter-Modul
- 3x männliche 3-pin JST Verbinder und weibliche Kabel
- 1x männlicher 4-pin JST Verbinder und weibliches Kabel
- Lochraster o.ä. um die Elektronik darauf zusammen zu löten

### Zwergenkörper

Wenn du den Datenzwerg in seinen Zwergenkörper stecken möchtest, benötigst du außerdem:

- 1x 3D gedrucktes Zwergenoberteil (siehe `models` Verzeichnis im GitHub Repository)
- 1x 3D gedrucktes Zwergenunterteil (siehe `models` Verzeichnis im GitHub Repository)
- 6x 6x1mm Neodymium Magnete
- Sekundenkleber

!!! note

    Es ist sehr empfehlenswert, das Zwergenoberteil mit einer 0,6mm Düse und 0,4mm Schichthöhe zu drucken. Das Modell ist für diese Kombination ausgelegt und funktioniert möglicherweise nicht mit anderen Düsen- oder Schichthöhen.

## Zusammenbau

### Mainboard

TODO

### Sensoren

TODO

### Stromversorgung

TODO

### Zwergenkörper

Mit dem Sekundenkleber die Magnete in die Löcher in Zwergenunter- und -oberteil kleben. Achte darauf, dass die Polarität stimmt, d.h. die Magnete ziehen sich an, wenn das Zwergenoberteil auf das Zwergenunterteil gesetzt wird. Die Magnete sollten bündig mit der Oberfläche abschließen.

## Firmware flashen

Stelle sicher, dass der Datenzwerg vom Strom getrennt ist. Ziehe den D1 mini vom Mainboard ab und verbinde ihn mit deinem Computer via USB.

Installiere Python 3.11. Check das [GitHub Repository](https://github.com/romses/Datenzwerg) aus und führe darin die folgenden Befehle aus:

1. `python -m venv venv`
2. `source venv/bin/activate`
3. `pip install -r requirements.txt`

Das installiert alle Abhängigkeiten, die für den Bau der Firmware und der Dokumentation benötigt werden, in ein virtuelles Environment und aktiviert es.

Dann navigiere zum `firmware` Verzeichnis. Kopiere `secrets-template.yaml` nach `secrets.yaml` und fülle deine WiFi- und InfluxDB2-Zugangsdaten ein. Dann führe die folgenden Befehle aus:

```
esphome -s name <gnome> datenzwerg.yaml run
```

Damit wird die Firmware für deinen Zwerg mit dem Namen `<gnome>` kompiliert und geflasht (d.h. wenn du z.B. die Firmware für den Zwerg mit dem Namen `zwerg` flashen möchtest, führe `esphome -s name zwerg datenzwerg.yaml run` aus).

Steck den D1 mini wieder auf das Mainboard und verbinde den Datenzwerg mit Strom. Er sollte sich mit deinem WiFi verbinden und Daten an die konfigurierte InfluxDB senden.
