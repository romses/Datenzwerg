# How to build a Datenzwerg

!!! todo

    Updaten wenn die englische Version fertig ist.

!!! warning
    
    Der Datenzwerg wurde für das [CCCamp23](https://events.ccc.de/camp/2023/infos/) entwickelt. Hardware, Firmware und Modelle wurden für einen bestimmten Zweck und eine bestimmte Nutzungsdauer entwickelt und sind möglicherweise nicht für andere Anwendungsfälle geeignet. Der Datenzwerg wird wie er ist ohne jegliche Garantie, Pläne zur Verbesserung oder Behebung oder andere Unterstützung bereitgestellt. Wenn du deinen eigenen Datenzwerg bauen möchtest, bist du auf dich allein gestellt.

## Voraussetzungen

Einen Datenzwerg zu bauen erfordert etwas Löterfahrung und 3D-Druckkenntnisse.

Die Firmware, die für den Datenzwerg zur Verfügung gestellt wird, erfordert, dass du ihr Zugangsdaten für ein vorhandenes WiFi-Netzwerk (SSID und Passwort) und auch Zugang zu einer InfluxDB2-Instanz (Host, Port, Organisations-ID, Bucket-Name und schreibfähiges Zugriffstoken) zur Verfügung stellst. Du musst diese Zugangsdaten in einer Datei namens secrets.yaml im Verzeichnis firmware angeben. Eine Vorlage für diese Datei findest du in firmware/secrets-template.yaml.
## Teile

### Elektronik

Um deinen eigenen Datenzwerg zu bauen, benötigst du folgende Teile:

| Menge | Teil | Funktion | Link | Preis |
| ----- | ---- | -------- | ---- | ----- |
| 1 | Wemos D1 Mini | MCU | [AliExpress](https://aliexpress.com/item/1005004967205772.html) | ~1.70€ |
| 1 | BME280 | Umweltsensor | [AliExpress](https://aliexpress.com/item/1005003676342598.html) | ~2.30€ |
| 1 | TP4056 | Lipo Charger | [AliExpress](https://aliexpress.com/item/32624444293.html) | ~0.50€ |
| 1 | VEML6075 | UV Sensor | [AliExpress](https://aliexpress.com/item/1005004653958045.html) | ~3.00€ |
| 1 | ADS1115 | 4 Port ADC | [AliExpress](https://aliexpress.com/item/32817162654.html) | ~1.70€ |
| 1 | GY-MAX4466 | Sound sensor | [Amazon](https://www.amazon.de/dp/B07YDG3VZF) | ~1.90€ |
| 1 | 5V boost converter | Power supply | (WIP) | (WIP) |
| 1 | 18650 LiPo battery | Power source | (WIP) | (on hand)[^1] |
| 1 | 18650 LiPo battery holder | Battery holder | [Amazon](https://www.amazon.de/dp/B08Y5R63YB) | ~0.64€ |
| 3 | male 3-pin JST connectors | Sensor & power connectors | (WIP) | (WIP) |
| 3 | female 3-pin JST cables | Sensor & power cables | (WIP) | (WIP) |
| 1 | male 4-pin JST connectors | I2C connector | (WIP) | (WIP) |
| 1 | female 4-pin JST cable | I2C cable | (WIP) | (WIP) |
| 1 | male 2-pin JST cable | Battery cable | (WIP) | (WIP) |
| 1 | female 2-pin JST cable | Battery cable | (WIP) | (WIP) |
| 1 | perfboard | Soldering board | [Amazon](https://www.amazon.de/gp/product/B085WJCRX8/) | ~0,80€ |

Zusätzlich benötigst du einen Lötkolben und Lötzinn.

!!! warning
    
    Wir benutzen einen BM**E** sensor. Diese werden oft mit den BM**P** sensoren verwechselt. Diesen fehlt aber der Sensor für Luftfeuchte.

### Zwergenkörper

Wenn du die Elektronik in einen Zwergenkörper bauen willst, benötigst du filgende Teile:

| Anzahl | Teil | Funktion | Link | Preis |
| ----- | ---- | -------- | ---- | ----- |
| 1 | 3D printed gnome body top | Gnome body | [Download](https://raw.githubusercontent.com/romses/Datenzwerg/main/models/datenzwerg_40p_1.2mm_top.stl) | (WIP) |
| 1 | 3D printed gnome body bottom | Gnome body | [Download](https://raw.githubusercontent.com/romses/Datenzwerg/main/models/datenzwerg_40p_1.2mm_bottom_filled.stl) | (WIP) |
| 6 | 6x1mm neodymium disc magnets | Connecting the top and bottom of the gnome body | [Amazon](https://www.amazon.de/dp/B007JTKX3Y) | ~1.85€ |
| 1 | ~3mm dickes und polierter 5mm Abschnitt eines 0A070GT Plexiglas XT Plexiglasstabes| UV transmissive rain cover for the UV sensor | [Sample from the manufacturer](https://www.plexiglas-shop.com/en-de/products/plexiglas-xt/sr0a070gt.html) | ~0.09€ |

Für den Zusammenbau benötigst du Sekundenkleber und/oder UV resin zum kleben und versiegeln.

!!! note

    Es wird dringend empfohlen, den Zwergenkörper mit einer 0.6mm Düse une einer Layer height von 0.4mm zu drucken.
    Das modell wurde speziell für diese Parameter angepasst. Möglicherweise kommt es zu unerwünschten Ergebnissen, 
    wenn eine andere Nozzle größe oder Layer height verwendet wird.

    Mit diesem Setup werden die Modelle mit 3 wänden und 3 Top/Bottom Layers sowie 20% infill gedruckt. 
    Am Besten verwendest du Treesupport.
    Das Drucken des Oberteils dauert ca. 5 Stunden, das Unterteil druckt in etwa einer Stunde.

!!! note

    Wir konnten ein 100mm Sample des XT Plexiglasstabes für etwa 3€ bekommen.
    Wir haben einen Dremel verwendet, um den Stab auf die entsprechende Länge zuzuschneiden.
    Die Besten Ergebnisse haben wir mit einem Dremel und diesem [Schneidetool](https://www.printables.com/model/113887-rod-and-tube-cutter-for-dremel-with-limiter) erhalten.
    Nach dem Zuschneiden haben wir die Teile mit 400er Schleifpapier und Polierpaste ("Elsterglanz")[^2] poliert.

!!! note

    Die O-Ringe werden oftmals als Dämpfungsringe für mechanische Tastaturen verkauft. Möglicherweise hast du entsprechende O-Ringe schon zu Hause vorrätig.  😅.

## Zusammenbau

### Mainboard

TODO

### Sensors

TODO

### Power supply

TODO

### Gnome body

Klebe die Magnete mit Sekundenkleber in die Löcher im Boden des Zwergenkörpers. Achte auf die richtige Polarität, d.h. die Magnete ziehen sich gegenseitig an, wenn der Zwergkörper oben auf den Boden gelegt wird. Die Magnete sollten bündig mit der Oberfläche des Zwergenkörpers abschließen.

Stecke den Acryl-Regenschutz in das obere der beiden Löcher und halte ihn von hinten mit dem Finger fest. Wenn sie nicht sofort passt, sleife das Loch im Druck vorsichtig größer, bis er passt. Er sollte bündig mit der Innenseite des Zwergenkörpers abschließen, es ist in Ordnung, wenn er auf der Vorderseite ein wenig übersteht. Achte unbedingt darauf auf, dass kein UV Resin auf die Oberfläche der Acrylscheibe gelangt. Das UV-resin darf nur auf die Ränder kommen. Härte es dann mit einer UV-Lampe aus.

!!! warning

    Achte darauf, dass kein UV-Resin auf die Oberfläche der Acrylscheibe gelangt. Wenn das passiert, wird sie dauerhaft getrübt sein.

Schraube den UV-Sensor in die Halterung. Lege dazu zuerst eine Unterlegscheibe auf die Mutter, dann den Sensor und dann einen der O-Ringe. Dann schiebe die Schraube von innen durch das Montageloch. Bringe einen weiteren O-Ring, eine weitere Unterlegscheibe und dann die Mutter an. Ziehe sie handfest an. Ziehe sie nicht zu fest an, da dies den Sensor beschädigen könnte.

## Flashen der Firmware

Vergewissere Dich, dass die Stromzufuhr zur Hauptplatine des Datenzwergs unterbrochen ist. Ziehe den D1 mini von der Hauptplatine ab und schließe ihn über USB an den Computer an.

!!! warning
    Das Mainboard verbinder D0 mit RST. So Lange diese beiden Pins miteinander verbunden sind, lässt sich der ESP nicht flashen.
 
Installiere Python 3.11. Clone das [GitHub repository](https://github.com/romses/Datenzwerg) und führe folgende Schritte aus:

1. `python -m venv venv`
2. `source venv/bin/activate`
3. `pip install -r requirements.txt`

Dadurch werden alle Abhängigkeiten, die zum Erstellen der Firmware und der Dokumentation erforderlich sind, in einer virtuellen Umgebung installiert und aktiviert.

Wechsel dann in das Verzeichnis `firmware`. Kopieren die secrets-template.yaml nach secrets.yaml und gib Deine WiFi- und InfluxDB2-Anmeldedaten ein. Führedann

```
esphome -s name <gnome> run datenzwerg.yaml
```

um die Firmware für den Datenzwerg mit dem Namen <gnome> zu kompilieren und zu flashen (wenn z.B. die Firmware für den Zwerg mit dem Namen `zwerg` geflashet werden soll, führe `esphome -s name zwerg datenzwerg.yaml` run aus).

Stecke den D1 mini wieder in die Hauptplatine und schließe ihn wieder an die Stromversorgung an. Es sollte sich mit dem WiFi verbinden und Daten an die konfigurierte InfluxDB senden.

[^1]: Wir haben die Lipos aus alten Powerbanks recycled
[^2]: Das geht am einfachsten, indem die Scheibe mit einer Zange festhalten wird. Zum Schleifen drücke die Scheibe gegen einen Schwingschleifer auf der niedrigsten Stufe und mit der richtigen Körnung. Zum Polieren reibe die Scheibe immer wieder von Hand auf einem Mikrofasertuch mit aufgetragener Polierpaste ab. Vergiss nicht, beide Seiten zu bearbeiten!
