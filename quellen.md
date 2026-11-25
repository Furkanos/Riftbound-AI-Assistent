# Quellen und Prüfstatus

Nutze gezielte Webabfragen im Chat. Speichere Referenzen und eigene
Kurznotizen, keine Rohkataloge, Inventar-Rohdaten oder Regelvolltexte.
Die beschriebenen Abrufe benötigen keine API-Keys. Halte bei späteren
optionalen Integrationen nur Umgebungsvariablennamen im Repo fest.

| Prüffeld | Live-Einstieg oder Eingabe | Rückfallweg |
|---|---|---|
| Regeln, Format, Bannstatus, Set-Freigabe | [Riot Rules Hub](https://playriftbound.com/en-us/rules-hub/); einschlägige offizielle Dokumente und Mitteilungen öffnen | Offizielle Veröffentlichung direkt suchen; ohne Beleg betroffene Felder getrennt als NICHT VERIFIZIERT ausweisen |
| Kartentext und Errata | Offizielle Kartenangaben und Errata über Riot | Kompaktpool für Kandidaten nutzen; entscheidende ungeklärte Interaktionen nur bedingt behandeln |
| Turnierlisten und Ergebnisse | [RiftBench Events](https://riftbench.com/decks/events), [Riftwatch Turniere](https://riftwatch.gg/tournaments/); wenn verfügbar Originalbericht von Riot oder Veranstalter | Anderen Einstieg oder Eventseite prüfen; ohne Listen nur belegte Ergebnisse, datierte Stichprobe oder Nutzerbeobachtungen berichten |
| Besitz | Hochgeladene normalisierte Sammlung | Fehlende Mengen abfragen; Besitz nicht aus Kartenpool, Preis oder Kaufliste ableiten |
| Budget | Datierte Angebote für konkrete Drucke mit Währung und bekannten Nebenkosten | Alternativangebot prüfen; ohne belastbaren Gesamtpreis Budget nicht bestätigen |

## Abrufprotokoll je Auftrag

`Prüffeld | URL/Referenz | Abrufdatum | Veröffentlichungsdatum | Format/Region/Event | Eventdatum/Stichtag | wirksam ab | Status`

Dokumentiere tatsächlich geöffnete Belege und fehlgeschlagene Abrufe.
Veröffentlichung, Abruf und Wirksamkeit getrennt halten. Fehlende Angaben
als `nicht angegeben` eintragen. Bei Konflikten Geltungsbereich und
Wirksamkeit prüfen; bleibt ein entscheidender Konflikt offen, beide
Belege nennen und keine Freigabe erteilen. Zähle dasselbe Event nicht
doppelt. Ein datierter lokaler Snapshot kann den Entwurf stützen, aber
keinen aktuellen Bann- oder Set-Status bestätigen.

## Prüfstufen

1. **CI:** CSV-Struktur, Kompaktberichte nur als Artefakte; keine
   Aussage zu Besitz, Budget oder aktueller Turnierlegalität.
2. **Lokaler Vollcheck:** Struktur, Pool und Bestand nach vorliegenden
   Daten. Kein Ersatz für den offiziellen Live-Abgleich.
3. **Judge im Chat:** Konkrete Liste anhand der wirksamen offiziellen
   Regeln, Bannliste und Set-Freigabe prüfen; auch ohne Skript. Bei
   fehlenden Pflichtbelegen keine aktuelle Turnierfreigabe.
