# Projektstand: Aktualisierung `wissen/08_archetypen.md`

**Dokumentationsstand:** 25.11.2026.
**Status:** Schritte 1, 2a und 2b sind abgeschlossen. Schritt 3 (Entscheidungen) und Schritt 4 (08 neu schreiben) sind offen. `wissen/08_archetypen.md` wurde noch nicht geändert.

> **Evidenzhinweis:** Alle Zahlen in diesem Dokument stammen aus dem Chatverlauf der Recherche (21.–25.11.2026). Die Belegdateien (PSV, Rohtexte, gespeicherte Standings-Seiten) liegen nur im Arbeitsbereich dieses Chats und **nicht im Repo**. Ein neuer Chat kann die Zahlen deshalb nicht aus dem Repo nachrechnen. Vor Schritt 4 müssen die Belege entweder ins Repo gelegt (nur auf Auftrag) oder die Zahlen neu erhoben werden.

## Korrekturen zur README (Stand Commit 4156116)

- **Nummernschreibweise `201/221`:** Die README beschreibt diese Stolperfalle ungenau. Gemeint ist: Riftwatch schreibt Drucke als `SFD-201/221`, das heißt Karte 201 von 221 (Setumfang). Das entspricht `SFD/201` in `wissen/07_legenden_uebersicht.md`. Liegt die Nummer **über** dem Setumfang (Beispiel Poppy `UNL-237/219`), ist es vermutlich ein Alternativdruck: `[BITTE PRÜFEN]`.
- **Pfadprüfung:** Die README-Pfade wurden nicht per Skript gegen das Repo validiert. `[BITTE PRÜFEN]`

## Ausgangslage

`wissen/08_archetypen.md` (Stand 17.11.2026) enthält 24 Legenden, 78 Turnierlisten-Links, 208 Kernkarten-Zeilen und 2 × `[BITTE PRÜFEN]` (Kennen `RBO-L-dotgg-414231`, Rek'sai `RBO-L-dotgg-389155`). Eine Zwischenzählung von 76 Links entstand, weil genau diese zwei Links ausgelassen wurden; 78 ist korrekt.

`wissen/07_legenden_uebersicht.md` führt inzwischen 34 Legendeneinträge mit 33 unterschiedlichen Namen (Diana doppelt: `UNL/197` und `UNL/234`). Gegenüber 08 fehlen also 9 neue RAD-Legenden.

## Methode und Filter

Eine Turnierliste zählt als **gültig**, wenn alle Punkte belegt sind:

1. Eventdatum ≥ 24.10.2026 (laut Zielseite).
2. Platz ≤ 64, belegt durch Standings. Endziffern in der URL sind kein Platzbeleg.
3. Kein Testevent (Beispiel: „Test Riftbound“, 24.10.2026).
4. Legende auf der Zielseite bestätigt.
5. Bannnamen-Check: alle zwölf Bannnamen aus `wissen/02_format.md` vollständig geprüft, kein Treffer.
6. Kartenpool-Gegenprobe: Kartennamen der Liste gegen `wissen/03_kartenpool.csv`.

Quellen in dieser Reihenfolge: riftbound.org (Legendenseite und Turnierübersicht), riftwatch.gg (Legendenprofil und All-lists-Ansicht), riftbench.com (Eventfilter). Zählungen nur per Skript über gespeicherte Seiten. Je Ansicht werden „gemeldet“ und „erfasst“ getrennt notiert. Ergebnisdateien sind PSV mit festen 8 Spalten; vor jedem Überschreiben eine `_vorher`-Sicherung.

„Keine Turnierlisten gefunden“ bedeutet: in den genannten Quellen kein Treffer innerhalb der Filter. Es bedeutet nicht, dass keine Liste existiert.

## Ergebnisse

### Block 1: 9 neue RAD-Legenden

Gesamt: **41 gültige Listen, 5 `[BITTE PRÜFEN]`** (darunter 2 Nexus-Night-Fälle bei Seraphine).

Bearbeitete Legenden laut Chatverlauf: Ekko, Evelynn, Jarvan IV, K'Sante, Mordekaiser, Orianna, Riven (`RAD/149`), Seraphine (`RAD/151`), Ziggs (`RAD/141`). Die Liste der Namen und die Aufteilung je Legende gegen 07 und die Beleg-PSVs prüfen: `[BITTE PRÜFEN]`.

### Block 2a: Kandidaten aus den 78 alten Links

21 Links erfüllen laut 08 Datum ≥ 24.10.2026 und Platz ≤ 64.

| Paket | Gültig | Nexus Night | Gesamt |
|---|---|---|---|
| 1 | 3 | 4 | 7 |
| 2 | 6 | 1 | 7 |
| 3 | 6 | 1 | 7 |
| Gesamt | 15 | 6 | 21 |

Nexus Night = „LDXP Sacramento – Nexus Night Constructed“. Der Platz ist bestätigt, das Datum ist zwischen 23.10. und 24.10.2026 unklar (riftbound.org nennt den 24.10.). Status bis zur Entscheidung: `[BITTE PRÜFEN]`, nicht gültig.

### Block 2b: Legenden ohne Link in 08

| Legende | Set/Nr laut 07 | Ergebnis | Belege |
|---|---|---|---|
| Poppy, Keeper of the Hammer | `UNL/203` | keine Turnierlisten gefunden | 8 Standings-Einträge belegt: 6 × Sacramento Showdown 25k (Plätze 284 bis 647), Regional Championship Europe Platz 290, Testevent Platz 31 (ausgeschlossen) |
| Renata Glasc, Chem-Baroness | `SFD/201` | keine Turnierlisten gefunden | 25 Events (24.10. bis 22.11.2026) gescannt; einziger Eintrag: Radiance Standard Challenge Friday, 06.11.2026, Platz 1746, kein Decklink |
| Sivir, Battle Mistress | `SFD/203` | keine Turnierlisten gefunden | 25 Events gescannt; einziger Eintrag: Nation Clash Saturday, 07.11.2026, Platz 606, kein Decklink |

Riftwatch führt für Renata und Sivir als jüngstes Ergebnis jeweils den 03.10.2026. RiftBench: je 0 Treffer bei Sacramento (723 Listen), Convergence IV (235 Listen) und Regional Championship Europe (315 Standings, Listen nicht veröffentlicht).

Vermerke:

- **Poppy:** Eine frühere Zählung von 12 Einträgen ist nicht reproduzierbar. Der Skriptlauf deckte nur die gespeicherten Sacramento-Seiten ab, nicht alle 25 Events. Riftwatch zeigt den Druck `UNL-237/219`. `[BITTE PRÜFEN]`
- **Renata:** Eine frühere Angabe `SFD/207` war falsch; `SFD/201` ist per grep in 07 bestätigt.
- **Sivir:** Die RiftBench-Filter-URLs und die riftbound.org-Profilansicht sind nicht protokolliert.

## Offene Entscheidungen (Schritt 3, Entscheidung beim Nutzer)

1. 6 Nexus-Night-Listen aus Block 2a: als gültig zählen oder mit Vermerk ausschließen?
2. 5 `[BITTE PRÜFEN]` aus Block 1: gleiche Regel wie Punkt 1 oder Einzelentscheidung?
3. Poppy-Druck `UNL-237/219`: als zweiten Druck in 07 und 08 vermerken (analog Diana)?
4. Optional: Poppy-Zählung über alle 25 Events nachholen.

## Schritt 4 (nicht begonnen)

`wissen/08_archetypen.md` neu entwerfen und schreiben. Nur auf ausdrücklichen Auftrag und erst nach Schritt 3. Die 24 alten Legendenabschnitte bleiben 1:1 erhalten; die 9 RAD-Legenden und die drei „keine Turnierlisten gefunden“-Einträge kommen dazu.

## Belegdateien (nur im Chat-Arbeitsbereich, nicht im Repo)

Unter anderem: `schritt2a_livepruefung_20261124.psv`, `paketsummen_8spalten_20261124.psv`, `schritt2b_poppy_final_20261124.psv`, `schritt2b_renata_20261124.psv`, `schritt2b_sivir_20261124.psv`, je Legende `*_rundeA_sammeln_*.psv` und `*_rundeB_pruefen_*.psv`, Deckrohtexte `P1-*`, `P2-*`, `P3-*` sowie gespeicherte Standings-Seiten (Sacramento, Convergence IV, Nexus Night).

Beim Erstellen dieser Dokumentation waren diese Dateien nicht erneut lesbar; die Zahlen oben wurden deshalb nicht noch einmal aus den Dateien nachgerechnet.
