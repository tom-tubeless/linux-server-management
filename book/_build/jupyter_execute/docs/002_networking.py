#!/usr/bin/env python
# coding: utf-8

# # Netzwerke
# 
# In diesem Kapitel wirst du selbst tätig.
# Mit dem Netzwerksimulator Filius kannst du die Grundlagen von Computer-Netzwerken auf dem eigenen Computer ausprobieren.
# Den Netzwerksimulator Filius gibt es für Windows, OSX und Linux.
# Du kannst Filius kostenlos unter [https://www.lernsoftware-filius.de](https://www.lernsoftware-filius.de) herunterladen und installieren.
# 
# ## Tipps beim Umgang mit Filius
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
# 2. Ändere Die Namen der Notebooks auf _Client_10_ und _Client_20_.
# 
# #### Aktionsmodus
# 
# 3. Installiere auf _Client_1_10_ die _Befehlszeilenkonsole_
# 4. Öffne die Befehlszeilenkonsole und trage folgenden Befehl ein: `ping 192.168.0.20`.
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
# > Schicke eine Nachricht und beobachte im Datenaustausch-Fenster was passiert.
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
# #### Aktionsmodus
# 
# 1. Installiere auf _Webserver_12_ den _"Text-Editor"_.
# 2. Öffne den _"Text-Editor"_. Klicke auf _"Datei" -> "Öffnen"_ und wähle im Ordner _"webserver"_ die Datei _"index.html"_ aus. Hinweis: _"index.html"_ muss im Feld _"Dateiname"_ stehen, dann auf _"Öffnen"_ klicken.
# 3. Die Homepage soll als _"Titel"_ deine Namen erhalten. Ändere den Titel indem du den Begriff _"Standardseite"_ durch deinen Namen ersetzt. `<title>Standardseite</title>`wird geändert in z.B. `<title>Tom Tubeless Homepage</title>`. Klicke anschließend auf _"Datei" -> "Speichern"_ und überprüfe deine Änderung im _Webbrowser_ von _Client_10_ oder _Client_11_ (Hinweis: Adresse lautet _192.168.0.12_).
# 4. Ändere die Überschrift ebenfalls ab. Ersetze _"Filius"_ durch deinen Namen. `<h2>FILIUS - Webserver</h2>` wird geändert in z.B. `<h2>Tubeless Webserver</h2>`. Klicke anschließend auf _"Datei" -> "Speichern"_ und überprüfe deine Änderung im _Webbrowser_ von _Client_10_ oder _Client_11_.
# 
# > Wenn die Übung 3 für dich kein Problem war, dann darfst du gerne auch das Bild auf der Homepage ändern.
# 
# 5. Installiere auf _Webserver_12_ die Software _"Datei-Explorer"_ und ändere das Bild der Homepage. Probiere es erst selbstständig, bevor du eine Lösung recherchierst. {cite:ps}`img2022`
# 
# > An den grün blinkenden Kabeln kann man den Netzwerkverkehr sehr gut erkennen!
# 
# 
# ## Nameserver (DNS)
# ### Übung 4
# Wenn du im Internet unterwegs bist, rufst du die Seiten nicht über die IP-Adresse auf, sondern du gibst einen Namen ein -> z.B. www.google.de.
# Dies richtest du jetzt für deine geänderte Homepage ein.
# 
# #### Entwurfsmodus
# 
# 1. Erweitere dein Netzwerk um einen Server (Name: _Nameserver_13_; IP-Adresse: _192.168.0.13_).
# 2. Verbinde den _Nameserver_13_ mit dem Switch.
# 
# #### Aktionsmodus
# 1. Installiere auf _Nameserver_13_ die Software _"DNS-Server"_.
# 2. Öffne die Software _"DNS-Server"_ und fülle die Felder wie folgt aus:
#    1. Domainname: _www.server-management.de_
#    2. IP-Adresse: _192.168.0.12_
# 3. Klicke danach auf _"Hinzufügen"_ und anschließend auf _"Starten"_.
# 
# #### Entwurfsmodus
# 1. Nun musst du an deinen Clients und Servern noch Einstellungen vornehmen. Gebe bei allen Geräten unter _"Domain Name Server"_ folgende IP-Adresse ein: _192.168.0.13_.
# 
# #### Aktionsmodus
# 1. Jetzt kannst du testen, ob deine Homepage unter der Adresse _www.server-management.de_ erreichbar ist. Öffne dazu in _Client_10_ oder _Client_11_ deinen Webbrowser und gebe die Adresse ein.
# 
# > Wenn deine Homepage erscheint hast du alles richtig gemacht. Falls die Meldung "Server konnte nicht erreicht werden!" angezeigt wird, hast du vermutlich den "DNS-Server" nicht gestartet.
# 
# ```{bibliography}
# :style: plain
# ```
