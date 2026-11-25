# Riftbound-AI-Assistent

**Stand dieser Dokumentation: 25.11.2026.** Das Repo verbindet Wissensdokumente, Kartendaten, lokale Decklisten und KI-Prompts mit reproduzierbaren Python-Prüfungen. Die Skripte unterstützen einen AI-Chat; sie ersetzen weder offizielle aktuelle Turnierregeln noch eine menschliche Quellenprüfung.

## Zweck & Zielbild

Ziel ist, Riftbound-Decks auf Basis der im Repo belegten Regeln, Karten- und Sammlungsdaten sowie nachvollziehbarer Metaquellen zu entwerfen und zu prüfen. Die Deckprüfung soll dabei die mechanische Kontrolle sein, nicht eine freie KI-Einschätzung. Das Repo enthält zudem Datenaufbereitung, Rollen-Tagging und Qualitätsauswertung.

## Einstieg für einen neuen AI-Chat

Lies in dieser Reihenfolge:

1. `ANLEITUNG.md`, `ANLEITUNG_DECKBAU.md` und `ANLEITUNG_DECKCHECK.md` für Nutzerablauf und Dateiformate.
2. `wissen/01_regeln_core.md`, `wissen/01_regeln_turnier.md`, `wissen/02_format.md` sowie – bei strittiger Regelauslegung – die zugehörigen PDF-Quelldokumente unter `wissen/`.
3. `wissen/03_kartenpool.csv` für Kartendaten; Inventardatei `wissen/Riftbound - Karten (Karten) 2026-11-09_18-40.csv` für Besitz und Preise; `wissen/Riftbound - Kartenkatalog (Kartenkatalog) 2026-11-09_19-01.csv` für Katalog-/Tag-/Druckdaten.
4. `wissen/04_meta_bericht.md`, `wissen/04_meta_turniere.csv`, `wissen/05_meta_decklisten.md`, `wissen/06_lokale_meta.md`, `wissen/06_regelklaerungen.md`, `wissen/07_legenden_uebersicht.md` und `wissen/08_archetypen.md` nur für die jeweils belegten Meta-/Legenden-/Archetyp-Aussagen.
5. `tools/datenbasis.py`, `tools/deckcheck.py`, `tools/deckqualitaet.py` und `.github/workflows/deckcheck.yml`, um den tatsächlich implementierten Ablauf und die Prüfumfänge zu verstehen.
6. `decks/VORLAGE.csv`, eine passende Deckdatei sowie ihre `ergebnis/<deck>_*`-Ausgaben; anschließend `prompts/rift-builder.md`, `prompts/rift-coach.md`, `prompts/rift-judge.md`, `prompts/rift-meta.md`.
7. Für Stand/Änderungen zusätzlich `PROJEKTSTAND.md` und Commit-Historie.

**Wahrheitshierarchie:** Für Struktur und Implementierung gilt der aktuelle Repo-Stand, nicht frühere Chatbehauptungen oder veraltete Doku. Für Regel-/Kartenfragen gilt die passende Primärquelle im Repo; Format- und Bannlistenstand ausdrücklich beachten. Inventar sagt Besitz, Kartenpool/ Katalog sagen nicht automatisch Besitz. Metaquellen belegen nur ihre dokumentierten Ereignisse, Datumsstände und Decklisten. Bei Abweichung nichts stillschweigend harmonisieren: Fundstelle nennen und `[BITTE PRÜFEN]` setzen.

## Repo-Struktur (rekursiver Überblick)

```text
.
├── README.md                         Projektübersicht und Einstieg (dieses Dokument)
├── PROJEKTSTAND.md                   Arbeitsstand der Archetypen-Aktualisierung (neu)
├── ANLEITUNG.md                      Deck hochladen und Ergebnisse finden
├── ANLEITUNG_DECKBAU.md              Quellen- und Buildprozess laut Doku
├── ANLEITUNG_DECKCHECK.md            Verwendung des automatisierten Checks
├── .github/workflows/deckcheck.yml   Trigger, Skriptfolge, Ergebnis-Commit
├── daten/
│   ├── karten_tags.csv               erzeugte Rollen-Tags
│   ├── legenden_engine.csv           Zuordnung Legende zu Engine-Tag
│   ├── namens_alias.csv              manuelle Namensalias-Korrekturen
│   ├── sammlung_normalisiert.csv     erzeugte normalisierte Besitzzusammenfassung
│   ├── tags_manuell.csv              manuelle Tag-Overrides
│   └── zuordnung_offen.csv           Inventarzeilen ohne sichere Kartenpool-Zuordnung
├── decks/
│   ├── VORLAGE.csv                   Semikolon-Decklisten-Vorlage
│   ├── khazix_locals_0eur_v1.csv … khazix_locals_0eur_v6.csv
│   ├── khazix_locals_50eur_v1.csv … khazix_locals_50eur_v3.csv
│   ├── khazix_midrange_v1.csv
│   ├── khazix_xp_ambush_v1.csv
│   ├── pyke_locals_budget0_v1.csv … pyke_locals_budget0_v3.csv
│   ├── rengar_aggro_v1.csv
│   └── rengar_fury_body_midrange_v1.csv
├── ergebnis/                         je Deck erzeugte Prüf- und Hilfsdateien
│   └── <deck>_{alternativen.md,deckcheck.csv,kartentexte.md,kaufliste.csv,legalitaet.md,qualitaet.md}
├── prompts/
│   ├── rift-builder.md               Deckbau-Assistent
│   ├── rift-coach.md                 Deck-Coaching
│   ├── rift-judge.md                 Regelfragen/Schiedsrichterrolle
│   └── rift-meta.md                  Meta-Auswertung
├── tools/
│   ├── datenbasis.py                 Inventar normalisieren, Zuordnungen und Tags erzeugen
│   ├── deckcheck.py                  Besitz-, Legalitäts- und Hilfsberichte erzeugen
│   └── deckqualitaet.py              Kurve, Engine- und Rollenwerte ausgeben
└── wissen/
    ├── 01_regeln_core.md             Core Rules (Übertragung/Arbeitsreferenz)
    ├── 01_regeln_turnier.md          Tournament Rules (Übertragung/Arbeitsreferenz)
    ├── 02_format.md                  Format, Bannliste und Regelzusammenfassung
    ├── 03_kartenpool.csv             Kartendatenbank im CSV-Format
    ├── 04_meta_bericht.md            Meta-Bericht
    ├── 04_meta_turniere.csv          Meta-Turnierdaten
    ├── 05_meta_decklisten.md         Decklistenbelege/Meta-Stichprobe
    ├── 06_lokale_meta.md             lokale Metadaten
    ├── 06_regelklaerungen.md         Regelklärungen
    ├── 07_legenden_uebersicht.md     Legenden-/Champion-/Sammlungsübersicht
    ├── 08_archetypen.md              Archetyp- und Turnierlisten-Auswertung
    ├── Riftbound - Karten (Karten) 2026-11-09_18-40.csv           Inventarexport
    ├── Riftbound - Kartenkatalog (Kartenkatalog) 2026-11-09_19-01.csv  Katalogexport
    ├── RiftboundCoreRulesRUP5_En_EN.pdf       Core Rules Quelle
    ├── RiftboundTournamentRulesRUP5_en_EN.pdf Tournament Rules Quelle
    ├── meta_bedrohungen.md            Bedrohungs-/Meta-Auswertung für Deckbau
    └── regeln_auszug.md               komprimierter Regel-Auszug für Deckbau
```

**Deckdateien genau:** `khazix_locals_0eur_v1.csv` bis `_v6.csv`, `khazix_locals_50eur_v1.csv` bis `_v3.csv`, `khazix_midrange_v1.csv`, `khazix_xp_ambush_v1.csv`, `pyke_locals_budget0_v1.csv` bis `_v3.csv`, `rengar_aggro_v1.csv`, `rengar_fury_body_midrange_v1.csv`. Es gibt im aktuellen `decks/`-Verzeichnis keine `kaisa.csv`.

**Ergebnisdateien:** Für die Deckdateien finden sich je nach vorhandenem Erzeugungsstand die Suffixe `alternativen.md`, `deckcheck.csv`, `kartentexte.md`, `kaufliste.csv`, `legalitaet.md` und `qualitaet.md`. Die jeweilige Vollständigkeit ist nicht garantiert; maßgeblich ist die tatsächliche `ergebnis/`-Dateiliste. Die Workflow-Outputs und `daten/` sind generiert und werden nicht von Hand als Datenquelle behandelt.

## Datenquellen & Dateiformate

- `decks/VORLAGE.csv`: Semikolon-getrennte Spalten `Anzahl;Name;Set;Nummer;Bereich`. Bereiche im Skript: `Legende`, `Champion`, `Main`, `Battlefield`, `Rune`, `Sideboard`; akzeptierte Aliasformen `Runen`, `Battlefields`.
- `wissen/03_kartenpool.csv`: Semikolon-getrennt; Kopf: `Name;Set;Nummer;Typ;Domäne;Kosten;Stats;Seltenheit;Kartentext;Status`. Die bisherige README nennt 1.259 Karten zum 07.11.; dieser Wert ist historisch und muss für aktuellen Umfang programmatisch neu gezählt werden.
- Inventar-CSV (Dateiname mit Zeitstempel 09.11.2026): Komma-getrennte Felder umfassen `Titel`, `Owned`, `PriceEUR`, `Typ`, `Domaenen`, `Tags`, `Supertyp`, `SetCode`, `Kartennummer` und weitere Katalog-/Textfelder. Die bisherige README sagte, Sammlung sei nicht im Repo; im aktuellen Baum liegt sie im Repo. Der Dateiname ist ein Exportstand, kein Beleg für aktuelle Besitz-/Marktpreise.
- Kartenkatalog-CSV (09.11.2026 19:01): Komma-getrennter Katalogexport; genaue Spalten/Datensatzanzahl hier nicht vollständig erfasst: `[BITTE PRÜFEN]`.
- `daten/sammlung_normalisiert.csv`: erzeugtes Semikolon-CSV mit `Name;Drucke;Typ;Domaene;Kosten;Stats;Besitz;Spielbar;Legal;Text`.
- `daten/karten_tags.csv`: erzeugte Rollen-Tags; Spalten `Name;Typ;Domaene;Kosten;Spielbar;Tag;Quelle;Beleg`; `auto` ist heuristisch, nicht als geprüft ausgeben.
- Meta-Bericht datiert in den bisherigen Repo-Notizen auf 11.11.2026; Daten älter als sechs Wochen ausdrücklich als veraltet markieren. Stand der einzelnen Dateien stets in der Datei selbst gegenprüfen.
- `wissen/08_archetypen.md` lokal dokumentiert Stand 17.11.2026: 24 Legenden (25 Legendeneinträge, da Diana doppelt gedruckt) und 78 Listen. In dieser Repo-Version gilt es als Quelle mit diesem Stand, nicht als Ergebnis der noch laufenden Aktualisierung.

## Funktionsweise: Ist

1. Deckbau-Anleitung fordert eine CSV unter `decks/`, Semikolon als Trennzeichen. Der Builder-Prompt beschreibt assistierten Entwurf; Prompts selbst führen keinen Code aus.
2. Commit/Push mit Änderungen in `decks/**`, `tools/**`, `wissen/**`, `daten/namens_alias.csv`, `daten/tags_manuell.csv`, `daten/legenden_engine.csv` oder `.github/workflows/deckcheck.yml` löst `.github/workflows/deckcheck.yml` aus. Zusätzlich ist `workflow_dispatch` aktiviert. Änderungen an anderen `daten/*`-Dateien lösen laut Pfadfiltern nicht direkt aus.
3. Workflow auf `ubuntu-latest` mit Python 3.x führt nacheinander `python tools/datenbasis.py`, `python tools/deckcheck.py`, `python tools/deckqualitaet.py` aus.
4. `datenbasis.py` liest das Inventar-CSV, `wissen/03_kartenpool.csv`, `wissen/02_format.md` und Alias-/manuelle Tagdateien. Es erzeugt `daten/sammlung_normalisiert.csv`, `daten/zuordnung_offen.csv` und `daten/karten_tags.csv`. Automatische Tags sind regelbasierte Vorschläge; manuelle Tags überschreiben sie.
5. `deckcheck.py` verarbeitet CSV-Decks unter `decks/` außer der Vorlage. Besitzabgleich nutzt Druck (Set/Nummer) und Namen-Fallback; Runen werden als unbegrenzt behandelt. Je Deck entstehen `<deck>_deckcheck.csv`, `<deck>_kaufliste.csv`, `<deck>_legalitaet.md`, `<deck>_kartentexte.md`, `<deck>_alternativen.md` unter `ergebnis/`. Legalitätsbericht testet u.a. Main inkl. Champion = 40, 1 Legende, 12 Runen, 3 unterschiedliche Battlefields, Kopiengrenze, Katalogabgleich, Bannliste, Sideboard ≤10, Domänen und Champion-/Signaturtag.
6. `deckqualitaet.py` erzeugt `<deck>_qualitaet.md` aus normalisierter Sammlung und Tags: Engine-Tag-Dichte, Kurve, günstige Units und Rollen. Das ist eine Qualitätsauswertung, kein Ersatz für Legalitätscheck.
7. Workflow hat `contents: write`, staged `ergebnis/ daten/` und committet nur bei Änderungen mit `Automated deckcheck results [skip ci]`.

**Wichtige Einschränkung:** `decks/sammlung_v4.csv` ist nicht vorhanden. Sollte eine Deckdatei dieses Namens oder ähnlichen Namens in späterem Stand existieren, ist sie kein Bestand ohne expliziten Nachweis. Doku nennt `sammlung_v4` teils widersprüchlich; tatsächliches Inventar ist der Zeitstempel-Export in `wissen/`.

## Funktionsweise: Soll / noch offen

Das Zielbild in älterer README beschreibt eine externe Google-Tabelle „Riftbound-Werkstatt“ als Recheninstanz; dieser Workflow berechnet nun Teile davon automatisiert. Ein automatischer KI-Deckbau, direkte Verbindung zu Google Sheets, aktueller Live-Meta-Import und vollständige Turnierlistenrecherche sind durch die hier geprüfte Workflow-Datei nicht implementiert. Budgetdeckel/Optimierung ist nicht Teil der Legalitätsprüfung. Qualitätsziele aus `ANLEITUNG_DECKBAU.md` (z. B. Engine ≥14, günstige Units ≥12, Removal ≥6) sind Doku-Ziele und kein Regeltest in `deckcheck.py`.

## Verbindliche Arbeitsregeln für die KI

- Repo als tatsächlichen Stand lesen; vor Änderungen Dateien lesen und Wirkungen/Trigger klären.
- Nicht im Kopf rechnen: Zeilen, Karten, Kopien, Quellen und Anteile per Skript zählen. Keine Zahlen oder Kartendetails erfinden.
- Kleinschrittig vorgehen und an Entscheidungspunkten STOPP einlegen; unklare Fakten mit `[BITTE PRÜFEN]` markieren.
- Aussagen an Datei, Tabellenzeile oder Link binden. Regellegalität, Tagzuordnung, Besitz und strategische Empfehlung voneinander trennen.
- Fehlende oder partiell belegte Listen niemals als „existiert nicht“ verallgemeinern. Meta älter als sechs Wochen als veraltet kennzeichnen.
- Decks im Vorlagenformat speichern; Runen gelten in diesem Prüfer als unbegrenzt. `sammlung_v4.csv` ≠ Inventar/Bestand.
- Keine Dateien im Repo ändern, außer der Nutzer fordert eine konkrete Änderung ausdrücklich an. Vor dem Commit nur den beauftragten Umfang ändern; SHA und Commit-Dateiliste berichten.

## Bekannte Stolperfallen & Dokumentationsabweichungen

- Alte README sagt, Inventar sei nicht im Repo und Regeln lägen lokal; das widerspricht dem aktuellen Baum: Inventar, Regel-Markdown und PDFs sind eingecheckt.
- Alte README beschreibt drei Assistenten, während vier Promptdateien (Builder, Coach, Judge, Meta) vorhanden sind.
- Alte README beschreibt Wissen als einzige Wahrheit, aber Skripte nutzen Inventar-/Katalogexporte und erzeugte `daten/`-Dateien; Prompt-/Anleitungstexte sind zudem nicht alle konsistent mit der Skriptwirklichkeit.
- `ANLEITUNG_DECKCHECK.md` sagt, nur `02_format.md`-Regeln würden geprüft; das Skript prüft zusätzlich Struktur-, Kopien-, Domänen-, Katalog- und Signaturbedingungen.
- `ANLEITUNG_DECKBAU.md` erwartet Erzeugung der Qualitätsdatei; Workflow tut dies, aber ihre Zahlen sind keine Legalitätsfreigabe. Workflow triggert nur definierte Pfade; nicht alle `daten/*`.
- Doppeldrucke: Kartennamen allein reichen nicht immer. Diana Scorn of the Moon existiert in der dokumentierten Legendenübersicht mit `UNL/197` und `UNL/234`; set/Nummer erhalten und Drucke nicht zusammenwerfen, wenn Regel-/Metadatenbezug relevant ist.
- Nummern wie `201` und `221` präzise als Drucknummern mit Set speichern. Der Prüfer normalisiert Buchstaben-Suffixe für Match, dennoch die Originalnummer nicht eigenmächtig ändern.
- `decks/kaisa.csv` fehlt aktuell, obwohl lokale Arbeitsdateien Kai'Sa-Entwurf/Deckcheck-Ausgaben enthalten. Nicht aus lokalen Dateien ins Repo übernehmen ohne Auftrag.
- Signature-Legalität/tag ist nicht Beweis spielerischer Pflicht oder optimaler Einbindung.
- Preis im Inventar ist Snapshot, kein Live-Angebot oder Budgetgarantie.

## Aktueller Stand (25.11.2026) & Roadmap

Der zuletzt sichtbare Repo-Commit ist vom 19.11.2026. Wissensdaten/Archetypen sind überwiegend ältere Snapshots; `08_archetypen.md` ist laut Dateikopf 17.11. Der Meta-Bericht ist laut Repo-/Chatkontext vom 11.11.2026. Einzelheiten der laufenden Aktualisierung stehen in [PROJEKTSTAND.md](PROJEKTSTAND.md); dessen Arbeitszahlen beruhen auf lokalen Notizen/Chatkontext und nicht auf im Repo eingecheckten Recherchebelegen.

**Laufende Recherche – laut Chatverlauf, nicht im Repo belegt:** Filter für neue Listen: Datum ≥24.10.2026, Platz ≤64, kein Testevent, Bannnamen-Abgleich und Kartenpool-Gegenprobe; genannte Quellen riftbound.org, riftwatch.gg, riftbench.com. Chat nennt 9 RAD-Legenden abgeschlossen (41 gültig, 5 `[BITTE PRÜFEN]`), 21 Kandidaten alter Belege (15 gültig, 6 Nexus Night mit unklarem 23./24.10.-Datum), Schritt 2b Poppy (UNL/203), Renata Glasc (SFD/201) und Sivir (SFD/203) ohne gefundene Turnierliste; Poppy mit Druckabweichung/Vermerken. Offen: Schritt 3 Entscheidungen und Schritt 4 Neuentwurf von 08 – letzteres ausdrücklich erst auf Auftrag. Diana hat die Drucke UNL/197 und UNL/234.

**Roadmap:** (1) Schritt 3 der 08-Recherche mit Primärbelegen/Entscheidung zu Prüffällen abschließen; (2) Beleg-/Zähldateien versionieren, sofern beauftragt; (3) 08 nur nach Auftrag aktualisieren; (4) Schema-, Datenstand- und Dokumentationsabweichungen kontrolliert auflösen; (5) Verbesserungen der Prüfungen separat spezifizieren und testen.

## Ansatzpunkte für Verbesserungen (Vorschläge, keine implementierten Änderungen)

- Aus tatsächlicher Triggerliste folgt: `daten/sammlung_normalisiert.csv` und `daten/karten_tags.csv` sind generierte Dateien, doch Änderungen an beliebigen `daten/*` lösen nicht alle Workflowpfade aus. Vorschlag: CI-Trigger und Generator-Abhängigkeiten gegenprüfen.
- Doku nennt teils Einschränkungen, die inzwischen nicht mehr gelten (Sammlung lokal; nur Regeln aus 02); Vorschlag: Anleitungen mit Skript und Workflow abgleichen.
- CSV-Schemata, Datenstand und Zählungen sind verstreut. Vorschlag: reproduzierbaren Inventarbericht/Schema-Prüfung ergänzen.
- Archetypen-Evidenz und laufende Recherche haben keine eingecheckten Schritt-PSVs; Vorschlag: mit Auftrag Quellen-/Entscheidungsprotokoll versionieren.
- Für Datenaktualisierungen mindestens Stichtag, Quelle, Prüfschritte und Unklarheiten dokumentieren.
