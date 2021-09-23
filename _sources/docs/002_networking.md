---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.10.3
kernelspec:
  display_name: Python 3.9
  language: python
  name: python3
---

# Netzwerke

In diesem Kapitel wirst du selbst tätig.
Mit dem Netzwerksimulator Filius kannst du die Grundlagen von Computer-Netzwerken auf dem eigenen Computer ausprobieren.
Den Netzwerksimulator Filius gibt es für Windows, OSX und Linux.
Du kannst Filius kostenlos unter [https://www.lernsoftware-filius.de](https://www.lernsoftware-filius.de) herunterladen und installieren.

## Tipps beim Umgang mit Filius kont

- Achte darauf, ob du die Arbeitsschritte im Entwurfsmodus ![](img/filius_entwurfsmodus.png) oder Aktionsmodus ![](img/filius_aktionsmodus.png) durchführen musst.

- Verkleinere im Aktionsmodus das Hauptfenster so, dass die Desktop-Ansichten der einzelnen Geräte neben das Hauptfenster passen.

* Benenne die Rechner nach ihrer Funktion und hänge einen Teil der IP-Adresse an (z.B. Webserver mit der IP-Adresse 192.168.0.3 bekommt den Namen „Webserver_0.3“).

* Verwende zur besseren Übersicht für Clients („normale“ Rechner) immer das Notebook.

* Verwende für Computer die eine Server-Funktion ausüben immer den Rechner.

* Wenn du mehr als zwei Computer verbinden möchtest, benötigst du einen Switch.

* Falls du zwei Netzwerke miteinander verbinden möchtest, benötigst du einen Vermittlungsrechner (Router).

* Über Modems können Netze rechnerübergreifend verbunden werden.

## Kleine LAN-Party: Verbindung von zwei Rechnern

### Übung 1

#### Entwurfsmodus

1. Erstelle ein Netzwerk mit zwei vernetzten Clients („normale“ Rechner)
2. Ändere Die Namen der Notebooks auf _Client_1_10_ und _Client_2_10_.

#### Aktionsmodus

3. Installiere auf _Client_1_10_ die _Befehlszeilenkonsole_
4. Öffne die Befehlszeilenkonsole und trage folgenden Befehl ein: `ping 192.168.0.10`.
5. Öffne mit einem Rechtsklick auf den entsprechenden Clienten _Datenaustausch anzeigen_.

#### Fragen

1. Was beobachtest du, wenn du dir die Befehlszeilenkonsole und die Datenaustausch-Fenster (Protokolle) beider Clients anschaust?
2. Wieviele Pakete werden verschickt?
3. Wieviele Pakete werden empfangen?
4. Was ist im Datenaustausch-Fenster von Client 1_10 passiert?
5. Was ist im Datenaustausch-Fenster von Client 2_10 passiert?

### Ping erklärt

Ping ist ein Diagnose-Programm, mit dem überprüft werden kann, ob ein bestimmtes Gerät in einem IP-Netzwerk erreichbar ist. Daneben es auch die Zeitspanne zwischen dem Aussenden eines Paketes zu diesem Host und dem Empfangen eines daraufhin unmittelbar zurückgeschickten Antwortpaketes an (= Paketumlaufzeit, meist round trip time oder RTT genannt). Das Programm wird üblicherweise als Konsolenbefehl ausgeführt.

<a href="http://www.youtube.com/watch?feature=player_embedded&v=y6GRa4skFtU
" target="_blank"><img src="http://img.youtube.com/vi/y6GRa4skFtU/0.jpg" 
alt="Ping" width="800" border="10" /></a>
