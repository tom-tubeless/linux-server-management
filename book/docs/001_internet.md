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

# Das Internet

Nach {cite:ps}`internet2021`

## Was ist das Internet?

Das Internet ist das beliebteste Computernetz der Welt.
Es begann als akademisches Forschungsprojekt im Jahr 1969 und wurde in den 1990er Jahren zu einem globalen kommerziellen Netz.
Heute wird es von mehr als 2 Milliarden Menschen auf der ganzen Welt genutzt.

Das Internet zeichnet sich noch durch seinen dezentralen Charakter aus.
Keine einzelne Personengruppe besitzt das Internet oder kontrolliert, wer sich mit ihm verbinden kann
Stattdessen betreiben Tausende von verschiedenen Organisationen ihre eigenen Netze und handeln freiwillige Zusammenschaltungsvereinbarungen aus.

Die meisten Menschen greifen über einen Webbrowser auf Internetinhalte zu.
Tatsächlich ist das Web so populär geworden, dass viele Menschen Internet und Web fälschlicherweise als Synonyme betrachten.
In Wirklichkeit ist das Web jedoch nur eine von vielen Internetanwendungen.
Andere beliebte Internetanwendungen sind E-Mail und BitTorrent.

## Wo ist das Internet?

Das Internet besteht im Wesentlichen aus drei Teilen:

- **Die letzte Meile** ist der Teil des Internets, der die Haushalte und kleinen Unternehmen mit dem Internet verbindet. In Deutschland werden Internetanschlüsse von Privathaushalten etwa durch Vodafone oder die Telekom zur Verfügung gestellt. Sie bieten Telefonleitungen, Kabelfernsehleitungen und immer mehr Glasfaser-Leitungen an. Zur letzten Meile gehören auch die Türme, die den Menschen den Internetzugang über ihr Handy ermöglichen. Drahtlose Internetdienste machen einen großen und wachsenden Anteil an der gesamten Internetnutzung aus. Neu ist schnelles Internet per Satellit.

- **Rechenzentren** sind Räume voller Server, die Benutzerdaten speichern und Online-Anwendungen und -Inhalte _hosten_. Einige befinden sich im Besitz großer Unternehmen wie Google und Facebook. Andere sind kommerzielle Einrichtungen, die vielen kleineren Websites ihre Dienste anbieten. Rechenzentren verfügen über sehr schnelle Internetverbindungen, so dass sie viele Nutzer gleichzeitig bedienen können. Rechenzentren können überall auf der Welt stehen, befinden sich aber oft in abgelegenen Gebieten, wo Land und Strom billig sind. Google, Facebook und Microsoft haben zum Beispiel große Rechenzentren in Iowa errichtet.

- **Das Backbone** besteht aus Langstreckennetzen - meist aus Glasfaserkabeln -, die Daten zwischen Rechenzentren und Verbrauchern übertragen. Der Backbone-Markt ist hart umkämpft. Backbone-Anbieter verbinden ihre Netze häufig an Internet-Austauschpunkten, die sich in der Regel in Großstädten befinden. Die Präsenz an IEPs macht es für Backbone-Anbieter viel einfacher, ihre Verbindungen zu anderen zu verbessern.

## Wer hat das Internet geschaffen?

Das Internet begann als ARPANET, ein akademisches Forschungsnetz, das von der Advanced Research Projects Agency (ARPA, heute DARPA) des Militärs finanziert wurde.
Das Projekt wurde von Bob Taylor, einem ARPA-Verwalter, geleitet, und das Netz wurde von der Beratungsfirma Bolt, Beranek und Newman aufgebaut.
Es wurde 1969 in Betrieb genommen.

1973 begannen die Software-Ingenieure Vint Cerf und Bob Kahn mit der Arbeit an der nächsten Generation von Netzwerkstandards für das ARPANET.
Diese Standards, die als _TCP/IP_ bekannt wurden, bildeten die Grundlage für das moderne Internet.
Am 1. Januar 1983 stellte das ARPANET auf die Verwendung von TCP/IP um.

In den 1980er Jahren verlagerte sich die Finanzierung des Internets vom Militär auf die National Science Foundation.
Die NSF finanzierte die Langstreckennetze, die von 1981 bis 1994 als Backbone für das Internet dienten.
Im Jahr 1994 übergab die Clinton-Regierung die Kontrolle über das Internet-Backbone an den privaten Sektor.
Seitdem wird es privat betrieben und finanziert.

## Wer leitet das Internet?

Niemand leitet das Internet.
Es ist als dezentrales Netz von Netzen organisiert.
Tausende von Unternehmen, Universitäten, Regierungen und andere Einrichtungen betreiben ihre eigenen Netze und tauschen auf der Grundlage freiwilliger Zusammenschaltungsvereinbarungen Daten untereinander aus.

Die gemeinsamen technischen Standards, die das Funktionieren des Internets ermöglichen, werden von einer Organisation namens _Internet Engineering Task Force_ verwaltet.
Die IETF ist eine offene Organisation; es steht jedem frei, an den Sitzungen teilzunehmen, neue Standards vorzuschlagen und Änderungen an bestehenden Standards zu empfehlen.
Niemand ist verpflichtet, die von der IETF gebilligten Standards zu übernehmen, aber der auf Konsens basierende Entscheidungsfindungsprozess der IETF trägt dazu bei, dass ihre Empfehlungen allgemein von der Internetgemeinschaft angenommen werden.

Die _Internet Corporation for Assigned Names and Numbers_ (ICANN) wird manchmal als für die Verwaltung des Internets zuständig bezeichnet.
Wie der Name schon sagt, ist die ICANN für die Verteilung von _Domänennamen_ (wie ww-gym.de) und _IP-Adressen_ zuständig.
Aber die ICANN kontrolliert nicht, wer sich mit dem Internet verbinden kann oder welche Art von Informationen über das Internet gesendet werden können.

## Was ist eine IP-Adresse?

_Internet-Protokoll-Adressen_ sind Nummern, mit denen sich Computer im Internet gegenseitig identifizieren.
Die IP-Adresse von ww-gym.de lautet zum Beispiel \(159.69.35.123gh\).

Eine Abteilung der ICANN, die so genannte Internet Assigned Numbers Authority, ist für die Verteilung der IP-Adressen zuständig, um sicherzustellen, dass nicht zwei verschiedene Organisationen dieselbe Adresse verwenden.

## Was ist IPv6?

Der derzeitige Internet-Standard, _IPv4_ genannt, lässt nur etwa 4 Milliarden IP-Adressen zu.
In den 1970er Jahren galt dies als eine sehr große Zahl, aber heute ist der Vorrat an IPv4-Adressen fast erschöpft.

Deshalb haben Internet-Ingenieure einen neuen Standard namens _IPv6_ entwickelt.
IPv6 ermöglicht eine unglaubliche Anzahl eindeutiger Adressen - die genaue Zahl ist 39 Ziffern lang - und stellt sicher, dass der Welt nie wieder die Adressen ausgehen werden.

Die Umstellung auf IPv6 verlief zunächst langsam.
Die technischen Arbeiten an der Norm wurden in den 1990er Jahren abgeschlossen, aber die Internet-Gemeinschaft sah sich mit einem ernsthaften Henne-Ei-Problem konfrontiert: Solange die meisten Menschen IPv4 verwendeten, gab es für niemanden einen Anreiz, zu IPv6 zu wechseln.

Als jedoch die IPv4-Adressen knapp wurden, beschleunigte sich die Einführung von IPv6.
Der Anteil der Nutzer, die sich über IPv6 mit Google verbinden, stieg von 1 Prozent Anfang 2013 auf 6 Prozent Mitte 2015.

## Was ist ein Paket?

Ein _Paket_ ist die Grundeinheit der über das Internet übertragenen Informationen.
Durch die Aufteilung von Informationen in kleine, leicht verdauliche Teile kann die Kapazität des Netzes effizienter genutzt werden.

Ein Paket besteht aus zwei Teilen.
Der _Header_ enthält Informationen, die dem Paket helfen, sein Ziel zu erreichen.
Dazu gehören die Länge des Pakets, seine Quelle und sein Ziel sowie ein Prüfsummenwert, mit dem der Empfänger feststellen kann, ob ein Paket während der Übertragung beschädigt wurde.
Nach dem Header folgen die eigentlichen Daten.
Ein Paket kann bis zu 64 Kilobyte an Daten enthalten, was ungefähr 20 Seiten Klartext entspricht.

Wenn bei Internet-Routern eine Überlastung oder andere technische Probleme auftreten, können sie diese durch einfaches Verwerfen der Pakete beheben.
Es liegt in der Verantwortung des sendenden Computers, zu erkennen, dass ein Paket sein Ziel nicht erreicht hat, und eine weitere Kopie zu senden.
Dieser Ansatz mag kontraintuitiv erscheinen, aber er vereinfacht die Kerninfrastruktur des Internets und führt zu einer höheren Leistung bei geringeren Kosten.

## Was ist das World Wide Web?

Das World Wide Web ist eine beliebte Methode zur Veröffentlichung von Informationen im Internet.
Das Web wurde 1991 von Timothy Berners-Lee, einem Computerprogrammierer bei der europäischen Forschungsorganisation CERN, entwickelt.
Es bot eine leistungsfähigere und benutzerfreundlichere Schnittstelle als andere Internetanwendungen.
Das Web unterstützte Hyperlinks, die es den Benutzern ermöglichten, mit einem einzigen Klick von einem Dokument zum anderen zu wechseln.

Im Laufe der Zeit wurde das Web immer ausgefeilter und unterstützte Bilder, Audio, Video und interaktive Inhalte.
Mitte der 1990er Jahre begannen Unternehmen wie Yahoo und Amazon.com, auf der Grundlage des Webs profitable Geschäfte zu machen.
In den 2000er Jahren wurden webbasierte Anwendungen mit vollem Funktionsumfang wie Yahoo Maps und Google Docs entwickelt.

1994 gründete Berners-Lee das _World Wide Web Consortium_ (W3C) als offizielle Standardisierungsorganisation für das Web.
Er ist immer noch Direktor des W3C und beaufsichtigt die Entwicklung von Webstandards.
Das Web ist jedoch eine offene Plattform, und das W3C kann niemanden dazu zwingen, seine Empfehlungen zu übernehmen.
In der Praxis sind die Organisationen mit dem größten Einfluss auf das Web Microsoft, Google, Apple und Mozilla, die Unternehmen, die die führenden Webbrowser herstellen.
Alle von diesen vier Unternehmen übernommenen Technologien werden de facto zu Webstandards.

Das Web ist so populär geworden, dass viele Menschen es heute als Synonym für das Internet selbst betrachten.
Aber technisch gesehen ist das Web nur eine von vielen Internetanwendungen.
Zu den anderen Anwendungen gehören E-Mail und BitTorrent.

## Was ist ein Webbrowser?

Ein Webbrowser ist ein Computerprogramm, mit dem Benutzer Websites herunterladen und anzeigen können.
Webbrowser gibt es für Desktop-Computer, Tablets und Mobiltelefone.

Der erste weit verbreitete Browser war Mosaic, der von Forschern an der Universität von Illinois entwickelt wurde.
Das Mosaic-Team zog nach Kalifornien und gründete Netscape, das 1994 den ersten kommerziell erfolgreichen Webbrowser entwickelte.

Die Popularität von Netscape wurde bald von Microsofts Internet Explorer in den Schatten gestellt, aber aus einer Open-Source-Version des Netscape-Browsers wurde der moderne Firefox-Browser.
Apple veröffentlichte 2003 seinen Safari-Browser, und Google brachte 2008 einen Browser namens Chrome heraus. Im Jahr 2015 war Chrome der beliebteste Webbrowser mit einem Marktanteil von rund 50 Prozent.
Internet Explorer (heute als Edge mit Chrome-Engine), Firefox und Safari hatten ebenfalls einen beträchtlichen Marktanteil.

## Was ist SSL?

_SSL_, die Abkürzung für _Secure Sockets Layer_, ist eine Familie von Verschlüsselungstechnologien, die es Webnutzern ermöglicht, die Privatsphäre der über das Internet übertragenen Informationen zu schützen.

Wenn Sie eine sichere Website wie Gmail.com besuchen, sehen Sie neben der URL ein Schloss, das anzeigt, dass Ihre Kommunikation mit der Website verschlüsselt ist.
Dieses Schloss soll signalisieren, dass Dritte nicht in der Lage sind, die von Ihnen gesendeten oder empfangenen Informationen zu lesen. Unter der Haube erreicht SSL dies, indem es Ihre Daten in eine verschlüsselte Nachricht umwandelt, die nur der Empfänger entziffern kann.
Wenn eine böswillige Partei das Gespräch abhört, sieht sie nur eine scheinbar zufällige Zeichenfolge, nicht aber den Inhalt Ihrer E-Mails, Facebook-Posts, Kreditkartennummern oder andere private Informationen.

SSL wurde 1994 von Netscape eingeführt.
In den ersten Jahren wurde es nur auf einigen wenigen Arten von Websites verwendet, z. B. auf Online-Banking-Sites.
In den frühen 2010er Jahren verwendeten Google, Yahoo und Facebook SSL-Verschlüsselung für ihre Websites und Online-Dienste.
In jüngster Zeit gibt es eine Bewegung hin zu einer allgemeinen Verwendung von SSL.
Im Jahr 2015 kündigte Mozilla an, dass künftige Versionen des Firefox-Browsers das Fehlen einer SSL-Verschlüsselung als Sicherheitsmangel behandeln würden, um alle Websites zu einem Upgrade zu bewegen.
Google hat mit Chrome den gleichen Schritt getan.

## Was ist das Domain Name System?

Das _Domain Name System_ (DNS) ist der Grund, warum Sie auf die Schulwebsite zugreifen können, indem Sie ww-gym.de in Ihren Browser eingeben und nicht eine schwer zu merkende numerische Adresse wie \(159.69.35.123\).

Das System ist hierarchisch aufgebaut.
Die .de-Domäne (Top level Domain) wird zum Beispiel von einem Unternehmen namens Verisign verwaltet.
Verisign weist Domänen wie google.com und ww-gym.de zu.
Die Inhaber dieser _Second-Level-Domains_ können wiederum _Sub-Domains_ wie [mail.ww-gym.de](https://mail.ww-gym.de) und [moodle.ww-gym.de](https://moodle.ww-gym.de) einrichten.

Da beliebte Websites Domänennamen verwenden, um sich in der Öffentlichkeit zu identifizieren, ist die Sicherheit des DNS zu einem zunehmenden Problem geworden.
Sowohl Kriminelle als auch Regierungsspione haben versucht, DNS zu kompromittieren, um sich als beliebte Websites wie facebook.com und gmail.com auszugeben und deren private Kommunikation abzufangen.
Ein Standard namens DNSSEC versucht, die DNS-Sicherheit durch Verschlüsselung zu verbessern, aber nur wenige Menschen haben ihn übernommen.

```{bibliography}
:style: plain
```
