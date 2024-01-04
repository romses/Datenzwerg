---
description: Du willst selbst einen Datenzwerg bauen? Hier findest du eine Bauanleitung!
---

# Wie man einen Datenzwerg baut

!!! warning "Warnung"
    
    Der Datenzwerg wurde für das [CCCamp23](https://events.ccc.de/camp/2023/infos/) entwickelt und später angepasst für den [37c3](https://events.ccc.de/congress/2023/infos/index.html). Hardware, Firmware und Modelle wurden für einen bestimmten Zweck und eine bestimmte Nutzungsdauer entwickelt und sind möglicherweise nicht für andere Anwendungsfälle geeignet. Der Datenzwerg wird wie er ist ohne jegliche Garantie, Pläne zur Verbesserung oder Behebung oder andere Unterstützung bereitgestellt. Wenn du deinen eigenen Datenzwerg bauen möchtest, bist du auf dich allein gestellt.

## Voraussetzungen

Einen Datenzwerg zu bauen erfordert etwas Löterfahrung und 3D-Druckkenntnisse.

Die Firmware, die für den Datenzwerg zur Verfügung gestellt wird, erfordert, dass du ihr Zugangsdaten für ein vorhandenes WiFi-Netzwerk (SSID und Passwort) und auch Zugang zu einer InfluxDB2-Instanz (Host, Port, Organisations-ID, Bucket-Name und schreibfähiges Zugriffstoken) zur Verfügung stellst. Du musst diese Zugangsdaten in einer Datei namens secrets.yaml im Verzeichnis firmware angeben. Eine Vorlage für diese Datei findest du in firmware/secrets-template.yaml.

## Teile

### Elektronik

Um deinen eigenen Datenzwerg zu bauen, benötigst du folgende Teile:

| Menge | Teil | Funktion | Link |
| ----- | ---- | -------- | ---- |
| 1     | Wemos D1 Mini | MCU | [AliExpress](https://aliexpress.com/item/1005004967205772.html), [Reichelt elektronik](https://www.reichelt.de/d1-mini-kompatibles-esp8266-board-v2-0-d1-mini-p253978.html?&nbc=1) |
| 1     | BME280 | Environment Sensor | [AliExpress](https://aliexpress.com/item/1005003676342598.html), [Reichelt elektronik](https://www.reichelt.de/kombo-sensor-luftdruck-luftfeuchtigkeit-temp--bme-280-p159825.html?&nbc=1) |
| 1     | SGP30 | TVOC/eCO2 Sensor | [AliExpress](https://aliexpress.com/item/1005004680000599.html) |
| 1     | VEML6075 | UV Sensor | [AliExpress](https://aliexpress.com/item/1005004653958045.html)|
| 1     | ADS1115 | 4 Port ADC | [AliExpress](https://aliexpress.com/item/32817162654.html), [Reichelt elektronik](https://www.reichelt.de/raspberry-a-d-wandler-ads1115-rpi-adc-1115-p316202.html?&nbc=1) |
| 1     | GY-MAX4466 | Sound sensor | [Amazon](https://www.amazon.de/dp/B07YDG3VZF), [Reichelt elektronik](https://www.reichelt.de/entwicklerboards-mikrofonverstaerker-max4466-debo-amp-mic-p235481.html?&nbc=1) |
| 3     | male 3-pin JST connectors + cables | Sensor & power connectors | [Amazon](https://www.amazon.de/gp/product/B08ZJ6JGB5) |
| 2     | male 4-pin JST connectors + cables | I2C connector | [Amazon](https://www.amazon.de/gp/product/B09LCRCTQG) |
| 2     | male 8-pin headers, male and female | ESP8266 connector | [Amazon](https://www.amazon.de/dp/B07DBY753C/) |
| 1     | male 10-pin header, male and female | ADS1115 connector | [Amazon](https://www.amazon.de/dp/B07DBY753C/) |

Zusätzlich benötigst du einen Lötkolben, Lötzinn, Litze und Schrumpfschlauch.

!!! warning "Warnung"
    
    Wir benutzen einen BM**E** sensor. Diese werden oft mit den BM**P** sensoren verwechselt. Diesen fehlt aber der Sensor für Luftfeuchte. Du kannst dein Modul mit der Hilfe [dieser Seite](https://homematic-forum.de/forum/viewtopic.php?t=68558) identifizieren.

!!! warning "Warnung"

    Falls du deinen Zwerg mit Batterien betreiben willst, verzichte auf den SGP30 Sensor. Er benötigt konstant Strom um korrekt zu arbeiten und funktioniert nicht mit Deep Sleep. Lass ihn einfach weg und pass die Firmware entsprechend an, wie unten beschrieben.

!!! note "Hinweis"

    Wir empfehlen, alle Teile der BOM zu verwenden. Wenn du jedoch etwas Geld sparen möchtest, kannst du die Sensoren direkt an das Board löten, und so das Geld für die JST Verbinder sparen. Du kannst auch den TP4056 weg lassen und die Kabel direkt an den LiPo löten. Sei jedoch gewarnt, dass das Modul Undervoltage-Schutz für den LiPo bereit stellt.

### Zwergenkörper

Wenn du die Elektronik in einen Zwergenkörper bauen willst, benötigst du folgende Teile:

| Anzahl | Teil | Funktion | Link |
| ----- | ---- | -------- | ---- |
| 1 | 3D printed gnome body top | Gnome body | [Download](https://raw.githubusercontent.com/romses/Datenzwerg/main/models/datenzwerg_40p_1.2mm_top.stl) |
| 1 | 3D printed gnome body bottom | Gnome body | [Download (closed)](https://raw.githubusercontent.com/romses/Datenzwerg/main/models/datenzwerg_40p_1.2mm_bottom.stl) or [Download (cable throughholes)](https://raw.githubusercontent.com/romses/Datenzwerg/main/models/datenzwerg_40p_1.2mm_bottom_poe.stl) |
| 6 | 6x1mm neodymium disc magnets | Connecting the top and bottom of the gnome body | [Amazon](https://www.amazon.de/dp/B007JTKX3Y) |
| 1 | ~3mm thick sanded and polished cut-off of a 5mm rod of 0A070GT Plexiglas XT | UV transmissive rain cover for the UV sensor | [Sample from the manufacturer](https://www.plexiglas-shop.com/en-de/products/plexiglas-xt/sr0a070gt.html) |

Für den Zusammenbau benötigst du Heißkleber, Sekundenkleber und UV reaktives Harz.

!!! note "Hinweis"

    Es wird dringend empfohlen, den Zwergenkörper mit einer 0.6mm Düse und einer Schichthöhe von 0.4mm zu drucken. Das Modell wurde speziell für diese Parameter entworfen und möglicherweise kommt es zu unerwünschten Ergebnissen, wenn eine andere Düsengröße oder Schichthöhe verwendet wird.

    Mit diesem Setup werden die Modelle mit 3 Wänden und 3 Top/Bottom-Layers sowie 20% Infill gedruckt und Tree-Supports gedruckt. Das Drucken des Oberteils sollte ca. 5 Stunden dauernd, das Unterteil etwa eine Stunde.

!!! note "Hinweis"

    Wir konnten ein 100mm Sample des XT Plexiglasstabes für etwa 3€ bekommen. Wir haben einen Dremel und [dieses 3D-gedruckte Schneidetool](https://www.printables.com/model/113887-rod-and-tube-cutter-for-dremel-with-limiter) genutzt, um den Stab zuzuschneiden, dann wurde der Abschnitt mit 240er und 400er Körnung glatt geschmirgelt und mit einer Universalpoliturpaste poliert ("Elsterglanz")[^2].

    ![Die vier Phasen eines Regenschutzes: Roher Abschnitt direkt vom Stab, mit 240er Körnung geschmirgelt, mit 400er Körning geschmirgelt, poliert.](assets/images/rain-cover-stages.jpg)

### Batteriemodul

Falls du den Datenzwerg mit Batterien betreiben willst, benötigst du zusätzlich folgende Teile:

| Anzahl | Teil | Funktion | Link |
| ----- | ---- | -------- | ---- |
| 1     | TP4056 | Lipo Charger | [AliExpress](https://aliexpress.com/item/32624444293.html) |
| 1     | 5V MT3608 boost converter | Power supply | [AliExpress](https://de.aliexpress.com/item/4001066566291.html) |
| 1     | 18650 LiPo battery | Power source | (on hand)[^1] |
| 1     | 18650 LiPo battery holder | Battery holder | [Amazon](https://www.amazon.de/dp/B08Y5R63YB) |
| 1     | male 2-pin JST cable male + JST cable female | Battery cable | [Amazon](https://www.amazon.de/GTIWUNG-Steckverbinder-Pin-Verbindungsstecker-Connector-Kabeldraht/dp/B07VYR7J49) |

### MicroUSB Modul

Falls du den Datenzwerg mit einem MicroUSB Kabel betreiben willst, benötigst du zusätzlich folgende Teile:

| Anzahl | Teil | Funktion | Link |
| ----- | ---- | -------- | ---- |
| 1     | Micro USB breakout board | Power connector | [Amazon](https://www.amazon.de/gp/product/B0BZDL6GKC/) |

Du solltest dann auch den Zwergenunterkörper mit Kabeldurchlass wählen.

## Zusammenbau

### Mainboard

=== "Platine"

    Wir haben für den Datenzwerg eine Platine designed und produzieren lassen. Du kannst die Gerberdateien [hier](https://github.com/romses/Datenzwerg/tree/main/hardware/pcbs/v1.1) finden.

    Das Datenzwerg-Mainboard auf solch einem Platine aufzubauen ist recht simpel. Löte die 4-pin JST Header in die ENV und TVOC Plätze und die 3-pin JST Header in die UV, SND und Power Plätze. Dann löte zwei 8-pin Buchsenleisten an den Platz des ESPs und eine 10-pin Buchsenleiste an den ADS1115-Platz.

    ![Die Datenzwerg-Mainboard-Platine in Version 1.1](assets/images/pcb-v1.1.jpg)

    Dann ist leider ein bisschen manuelle Nacharbeit nötig: Verlöte auf der Unterseite der Platine ein Stück Draht zwischen dem 3v3 Pin des ESP8266 und dem 3v3 Pin von TVOC oder ENV Sensor.

    ![Die Datenzwerg-Mainboard-Platine in Version 1.1 mit dem angelöteten Draht](assets/images/pcb-v1.1-rework.jpg)

=== "Handgelötet auf Lochraster (nur v1.0)"

    Das Mainboard ist der schwierigste Teil des Zusammenbaus. Wir empfehlen,     zuerst die 3V3 Stromversorgung (orange im Fritzing-Schaltplan) und die GND     Verbindungen (schwarz) zu verdrahten, dann die I2C Verbindung (grün und     gelb).
    
    Das sind die kompliziertesten Verbindungen. Als nächstes die 5V     Verbindungen (rot) und schließlich die analogen Signale (cyan).
    
    ![Der Fritzing-Schaltplan des Datenzwerg-Mainboards](assets/images/    Datenzwerg-Komplett-Fritzing.png)
    
    Der Fritzing-Schaltplan zeigt den ESP in seiner Standardorientierung. Wir     haben uns jedoch entschlossen, den ESP umzuwenden. Das Diagramm zeigt auch     den ADS1115 in einer gedrehten Orientierung. Dies macht das     Fritzing-Diagramm viel einfacher zu verstehen.
    
    ![PCB-Skizze des Datenzwerg-Mainboards](assets/images/Datenzwerg-pcb.svg)    {: style="width:100%"}
    
    Die PCB-Skizze zeigt den ESP und den ADS1115 in der korrekten     Orientierung. Diese Skizze ist viel näher an unseren handgelöteten     Platinen als im Fritzing-Diagramm gezeigt.
    
    ![Das Datenzwerg-Mainboard auf Lochraster](assets/images/    Datenzwerg-komplett.png)
    
    !!! note "Hinweis"
        
        Wir haben eine spezielle Art von Lochraster verwendet. Die Gruppierung     von jeweils drei Löchern erleichtert die Organisation der Kabel     erheblich.
        
        ![Lochrasterbeispiel](assets/images/perfboard.png)

Sobald du das Mainboard verlötet hast, empfehlen wir, die Unterseite in breiten Streifen mit Kaptonband abzudecken, um Kurzschlüsse zu vermeiden. Alternativ kannst du auch Isolierband verwenden.

!!! note "Hinweis"

    Dinge, die nach dem Löten zu überprüfen sind:

    - UV-Sensor, BME280, SGP30 und Soundsensor werden mit 3V3 vom ESP versorgt.
    - ADS1115 und ESP sind mit 5V von der Stromversorgung versorgt.
    - Alle GNDs sind verbunden.
    - Keine Kurzschlüsse zwischen den Pins, insbesondere zwischen benachbarten Pins, Brücken können schnell entstehen. Verwende ein Multimeter, um Kurzschlüsse zu überprüfen.

### Sensoren

#### UV- und Schallsensor

Die UV- und Schallsensoren werden an JST Verbindungskabel gelötet, um die Sensoren austauschbar zu machen. Stelle das Potentiometer auf der Rückseite des Schallsensors (vorsichtig!) auf die linke (im Uhrzeigersinn) Position ein, das setzt den Verstärkungsfaktor auf 25x, was der Firmware entspricht. Verpacke die Lötstellen in  Schrumpfschlauch, um sie zu schützen und die Wahrscheinlichkeit von Kurzschlüssen zu verringern.

![Das UV-Modul](assets/images/UV-module.png)
![Das UV-Modul als Fritzing-Zeichnung, die zeigt, wie der JST Verbinder anzubringen ist. Orange an VCC, Schwarz an GND, Gelb an Signal](assets/images/UV-module-fritzing.png)

#### BME280 und SGP30

Der BME280 Sensor wird an einen 4-poligen JST Verbinder gelötet. Verwende Schrumpfschlauch, um die Lötstellen zu schützen und die Wahrscheinlichkeit von Kurzschlüssen zu verringern.

![Das BME Modul](assets/images/BME280.png)
![Das BME module als Fritzing-Schaltplan, worauf zu sehen ist, wie der JST Header zu verbinden ist. Orange an Vin, Schwarz an GND, Gelb an SCL, Grün an SDA](assets/images/BME280-fritzing.png)

!!! note "Hinweis"

    Die Temperatur im Inneren des Datenzwergs kann sehr viel wärmer werden als die Außentemperatur. Wir haben festgestellt, dass die Temperaturmessungen bei direkter Sonneneinstrahlung selbst dann noch erhöht waren, wenn wir den Sensor durch den Schlitz im Datenzwerggehäuse nach außen verlegt haben, möglicherweise aufgrund der Abwärme des erhitzten Gehäuses selbst. Wir haben uns entschieden, mit diesem Problem zu leben und es einfach in der Dokumentation zu erwähnen. Ein anderes Gehäusedesign könnte dieses Problem möglicherweise lösen.

### Stromversorgnung

=== "Batterieversorgung"

    Die Stromversorung ist die zweite komplexe Komponente des Datenzwergs.
    
    In unserem ursprünglichen Design war es der Plan, die LiPos direkt mittels     der verbauten TP4056 Module zu laden. In unseren Tests zeigte sich jedoch,     dass diese Module beim Laden sehr sehr heiß werden - wir sahen bis zu 86°    C, und das war uns zu heiß, um sie auf dem möglicherweise sehr trockenen     Feld des CCCamps zu laden.
    
    Aus diesem Grund laden wir die LiPos extern in einem handelsüblichen LiPo     Ladegerät. Wir haben die Module jedoch behalten, um eine Tiefentladung zu     verhindern.
    
    Die BAT+ und BAT- Anschlüsse sind mit VIN+ und VIN- von Boost-Konvertern     verbunden, die auf 5V Ausgangsspannung eingestellt sind. Sowohl der     ADS1115 als auch der ESP8266 können mit 3V3 betrieben werden. Der TP4056     liefert jedoch die Batteriespannung. Daher war der einfachste Weg, die     Spannung auf 5V zu erhöhen, indem wir einen Boost-Konverter verwendeten,     um sowohl den ESP8266 als auch den ADS1115 mit Strom zu versorgen. Dies     hat auch den Vorteil, dass wir die Batteriespannung mit dem ADS1115 messen     können, der Spannungen bis Vcc + 0,3V messen kann. Wir haben daher den     dritten Draht des 3-poligen JST-Steckers, der für die Verbindung zum     Mainboard verwendet wird, mit VIN+ verbunden, während die anderen beiden     Drähte mit VOUT+ und VOUT- verbunden sind.
    
    Verwende Schrumpfschlauch, um die Lötstellen zu schützen und die     Wahrscheinlichkeit von Kurzschlüssen zu verringern.
    
    ![Das zusammengebaute Stromversorgungsmodul](assets/images/Power-Module.    png)
    ![Die Stromversorung als Fritzing-Schaltplan, Verbindungen wie im Text     beschrieben.](assets/images/Power-Module-fritzing.png)

=== "MicroUSB-Versorgung"

    Das MicroUSB-Modul ist wesentlich simpler als das Batteriemodul. Es ist schlicht ein MicroUSB-Breakout-Board an einem 3-pin JST Kabel, rot an 5V, schwarz an GND. Gelb ist einfach abgeschnitten. Verwende Schrumpfschlauch, um die Lötstellen zu schützen und die     Wahrscheinlichkeit von Kurzschlüssen zu verringern.

    ![Das zusammengebaute MicroUSB-Modul](assets/images/microusb-cable.jpg)

### Zwergenkörper

Klebe die Magnete mit Sekundenkleber in die Löcher im Boden des Zwergenkörpers. Achte auf die richtige Polarität, d.h. die Magnete ziehen sich gegenseitig an, wenn Ober- und Unterteil aufeinander gesetzt werden. Die Magnete sollten bündig mit der Oberfläche des Zwergenkörpers abschließen.

Stecke den Acryl-Regenschutz in das obere der beiden Löcher und halte ihn von hinten mit dem Finger fest. Wenn sie nicht sofort passt, sleife das Loch im Druck vorsichtig größer, bis er passt. Er sollte bündig mit der Innenseite des Zwergenkörpers abschließen, es ist in Ordnung, wenn er auf der Vorderseite ein wenig übersteht. Achte unbedingt darauf auf, dass kein UV-Resin auf die Oberfläche der Acrylscheibe gelangt. Das UV-Resin darf nur auf die Ränder kommen. Härte es dann mit einer UV-Lampe aus.

!!! warning "Warnung"

    Achte darauf, dass kein UV-Resin auf die Oberfläche der Acrylscheibe gelangt. Wenn das passiert, wird sie dauerhaft getrübt sein.

Verwende einen kleinen Schraubenzieher oder ein anderes Werkzeug um den UV-Sensor an seinem Schrumpfschlauch festzuhalten. Klebe Heißkleber auf den Schrumpfschlauch und befestige den Sensor an seinem Platz so dass der eigentliche Sensor im Zentrum des Acrylfensters zu sehen ist.

Klebe Heißkleber auf den Schrumpfschlauch des BME Sensors und klebe diesen an seinen Platz neben dem Schlitz im unteren Bereich des Oberteils, mit dem Sensor nach unten zeigend.

## Flashen der Firmware

Vergewissere Dich, dass die Stromzufuhr zur Hauptplatine des Datenzwergs unterbrochen ist. Ziehe den D1 mini von der Hauptplatine ab und schließe ihn über USB an den Computer an.

!!! note "Hinweis"

    Das Mainboard verbindet D0 mit RST. Solange diese beiden Pins miteinander verbunden sind, lässt sich der ESP nicht flashen.
 
Installiere Python 3.11. Clone das [GitHub repository](https://github.com/romses/Datenzwerg) und führe folgende Schritte aus:

1. `python -m venv venv`
2. `source venv/bin/activate`
3. `pip install -r requirements.txt`

Dadurch werden alle Abhängigkeiten, die zum Erstellen der Firmware und der Dokumentation erforderlich sind, in einer virtuellen Umgebung installiert und aktiviert.

Wechsel dann in das Verzeichnis `firmware`. Kopieren die secrets-template.yaml nach secrets.yaml und gib Deine WiFi-, MQTT- und InfluxDB2-Anmeldedaten ein und vergib ein OTA-Passwort, falls gewünscht. Führe dann

```
esphome -s name <zwerg> -s eco2_baseline <eco2 baseline> -s tvoc_baseline <tvoc baseline> run datenzwerg.yaml
```

um die Firmware für den Datenzwerg mit dem Namen <zwerg>, der eCO2 Baseline `<eco2 baseline>` und der TVOC Baseline `<tvoc baseline>` zu kompilieren und zu flashen.

Wenn z.B. die Firmware für den Zwerg mit dem Namen `zwerg`, der eCO2 Baseline `0x7F10` und der TVOC Baseline `0x88B4` geflashet werden soll, führe `esphome -s name zwerg -s eco2_baseline 0x7F10 -s tvoc_baseline 0x88B4 run datenzwerg.yaml` aus. Falls du noch keine Baseline Werte hast, kannst du sie auch weglassen: `esphome -s name zwerg run datenzwerg.yaml`.

!!! warning "Warnung"

    Die aktuell eingecheckte Fassung der Firmware is optimiert für v1.1 mit MicroUSB-Versorgung, da der eCO2/TVOC-Sensor, der in v1.1 hinzugefügt wurde, eine konstante Stromversorgung benötigt, um sinnvolle Werte auszuspucken.

    Falls du die Firmware mit einem batteriegetriebenen Zwerg verwenden willst, musst du die Konfiguration anpassen, um Deep Sleep zu aktivieren, in dem du das `deepsleep` package in `firmware/datenzwerg.yaml` aktivierest und die `tvoc` und `uptime` Packages auskommentierst:

    ```yaml
    packages:
      base: !include packages/base.yaml # base v1.0 sensor package
      #tvoc: !include packages/tvoc.yaml # TVOC sensor added in v1.1, incompatible to battery power
      deepsleep: !include packages/deepsleep.yaml  # enable this on battery power
      #uptime: !include packages/uptime.yaml  # disable this on battery power
    
      # these should not be enabled in production
      #ota: !include packages/ota.yaml
      #webserver: !include packages/webserver.yaml

    ```

    Wenn du ohne das `tvoc` Package die Firmware kompilierst, kannst du auch die `eco2_baseline` und `tvoc_baseline` Parameter weg lassen.

Stecke den D1 mini wieder in die Hauptplatine und schließe ihn wieder an die Stromversorgung an. Es sollte sich mit dem WiFi verbinden und Daten an die konfigurierte InfluxDB senden.

[^1]: Wir haben die Lipos aus alten Powerbanks recycled
[^2]: Das geht am einfachsten, indem die Scheibe mit einer Zange festhalten wird. Zum Schleifen drücke die Scheibe gegen einen Schwingschleifer auf der niedrigsten Stufe und mit der richtigen Körnung. Zum Polieren reibe die Scheibe immer wieder von Hand auf einem Mikrofasertuch mit aufgetragener Polierpaste ab. Vergiss nicht, beide Seiten zu bearbeiten!
