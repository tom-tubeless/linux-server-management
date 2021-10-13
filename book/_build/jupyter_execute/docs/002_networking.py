#!/usr/bin/env python
# coding: utf-8

# # Netzwerke
# 
# In diesem Kapitel wirst du selbst tätig.
# Mit dem Netzwerksimulator Filius kannst du die Grundlagen von Computer-Netzwerken auf dem eigenen Computer ausprobieren.
# Den Netzwerksimulator Filius gibt es für Windows, OSX und Linux.
# Du kannst Filius kostenlos unter [https://www.lernsoftware-filius.de](https://www.lernsoftware-filius.de) herunterladen und installieren.
# 
# ## Tipps beim Umgang mit Filius kont
# 
# - Achte darauf, ob du die Arbeitsschritte im Entwurfsmodus ![](img/filius_entwurfsmodus.png) oder Aktionsmodus ![](img/filius_aktionsmodus.png) durchführen musst.
# 
# - Verkleinere im Aktionsmodus das Hauptfenster so, dass die Desktop-Ansichten der einzelnen Geräte neben das Hauptfenster passen.
# 
# * Benenne die Rechner nach ihrer Funktion und hänge einen Teil der IP-Adresse an (z.B. Webserver mit der IP-Adresse 192.168.0.3 bekommt den Namen „Webserver_0.3“).
# 
# * Verwende zur besseren Übersicht für Clients („normale“ Rechner) immer das Notebook.
# 
# * Verwende für Computer die eine Server-Funktion ausüben immer den Rechner.
# 
# * Wenn du mehr als zwei Computer verbinden möchtest, benötigst du einen Switch.
# 
# * Falls du zwei Netzwerke miteinander verbinden möchtest, benötigst du einen Vermittlungsrechner (Router).
# 
# * Über Modems können Netze rechnerübergreifend verbunden werden.
# 
# ## Kleine LAN-Party: Verbindung von zwei Rechnern
# 
# ### Übung 1
# 
# #### Entwurfsmodus
# 
# 1. Erstelle ein Netzwerk mit zwei vernetzten Clients („normale“ Rechner)
# 2. Ändere Die Namen der Notebooks auf _Client_1_10_ und _Client_2_10_.
# 
# #### Aktionsmodus
# 
# 3. Installiere auf _Client_1_10_ die _Befehlszeilenkonsole_
# 4. Öffne die Befehlszeilenkonsole und trage folgenden Befehl ein: `ping 192.168.0.10`.
# 5. Öffne mit einem Rechtsklick auf den entsprechenden Clienten _Datenaustausch anzeigen_.
# 
# #### Fragen
# 
# 1. Was beobachtest du, wenn du dir die Befehlszeilenkonsole und die Datenaustausch-Fenster (Protokolle) beider Clients anschaust?
# 2. Wieviele Pakete werden verschickt?
# 3. Wieviele Pakete werden empfangen?
# 4. Was ist im Datenaustausch-Fenster von Client 1_10 passiert?
# 5. Was ist im Datenaustausch-Fenster von Client 2_10 passiert?
# 
# ### Ping erklärt
# 
# Ping ist ein Diagnose-Programm, mit dem überprüft werden kann, ob ein bestimmtes Gerät in einem IP-Netzwerk erreichbar ist. Daneben es auch die Zeitspanne zwischen dem Aussenden eines Paketes zu diesem Host und dem Empfangen eines daraufhin unmittelbar zurückgeschickten Antwortpaketes an (= Paketumlaufzeit, meist round trip time oder RTT genannt). Das Programm wird üblicherweise als Konsolenbefehl ausgeführt.
# 
# <a href="http://www.youtube.com/watch?feature=player_embedded&v=y6GRa4skFtU
# " target="_blank"><img src="http://img.youtube.com/vi/y6GRa4skFtU/0.jpg" 
# alt="Ping" width="800" border="10" /></a>
# 
# ## Switch und Webserver-Software
# 
# ### Übung 2
# 
# #### Entwurfsmodus
# 
# 1. Erstelle ein Netzwerk mit zwei Clients und einem Server (Du benötigst hierzu zwei Notebooks, einen Rechner, einen Switch und Kabel).
# 
# 2. Bennene die Rechner folgensermaßen
# 
# | Name         | IP-Adresse   |
# | ------------ | ------------ |
# | Client_10    | 192.168.0.10 |
# | Client_11    | 192.168.0.11 |
# | Webserver_12 | 192.168.0.12 |
# 
# #### Aktionsmodus
# 
# 3. Installiere auf dem _Webserver_12_ die Software _"Webserver"_ und starte ihn
#    anschließend.
# 4. Installiere auf beiden _Clients_ einen _"Webbrowser"_.
# 5. Du möchtest nun die Webseite des _Webservers_ aufrufen. Öffne dazu den _Webbrowser_ deines _Clients_ und trage in die Adresszeile die _IP-Adresse_ des _Webservers_ ein (siehe Tabelle).
# 6. Hat alles geklappt? Dann mache mit Übung 3 weiter.
# 
# ### Übung 3
# 
# Die Webseite gefällt dir nicht, deshalb möchtest du Änderungen daran vornehmen.
# Hierzu musst du vorher aber noch einige Arbeitsschritte ausführen.
# 
# #### Entwurfsmodus
# 
# 1. Installiere auf _Webserver_12_ den _"Text-Editor"_.
# 2. Öffne den _"Text-Editor"_. Klicke auf _"Datei" -> "Öffnen"_ und wähle im Ordner _"webserver"_ die Datei _"index.html"_ aus. Hinweis: _"index.html"_ muss im Feld _"Dateiname"_ stehen, dann auf _"Öffnen"_ klicken.
# 3. Die Homepage soll als _"Titel"_ deine Namen erhalten. Ändere den Titel indem du den Begriff _"Standardseite"_ durch deinen Namen ersetzt. `<title>Standardseite</title>`wird geändert in z.B. `<title>Tom Tubeless Homepage</title>`. Klicke anschließend auf _"Datei" -> "Speichern"_ und überprüfe deine Änderung im _Webbrowser_ von _Client_10_ oder _Client_11_ (Hinweis: Adresse lautet _192.168.0.12_).
# 4. Ändere die Überschrift ebenfalls ab. Ersetze _"Filius"_ durch deinen Namen. `<h2>FILIUS - Webserver</h2>` wird geändert in z.B. `<h2>Tubeless Webserver</h2>`. Klicke anschließend auf _"Datei" -> "Speichern"_ und überprüfe deine Änderung im _Webbrowser_ von _Client_10_ oder _Client_11_.
# 5. Installiere auf _Webserver_12_ die Software _"Datei-Explorer"_ und ändere das Bild der Homepage. Probiere es erst selbstständig, bevor du eine Lösung recherchierst.
