# Riftbound-AI-Assistent

Wissensbasis und Systemprompts für drei My-Mammouth-Assistenten (Rift-Meta, Rift-Builder, Rift-Judge),
die aus Kartensammlung + Budget das stärkste legale Riftbound-Turnierdeck (Standard Constructed 1v1) bauen.

**Grundprinzip:** Die KI DENKT (Synergien, Meta, Matchups), die Google-Tabelle „Riftbound-Werkstatt“ RECHNET
(Besitz, Fehlend, Kosten).

## Ordner

| Ordner | Inhalt |
|---|---|
| `wissen/` | Regeln, Format, Kartenpool, Meta-Daten (einzige Quelle der Wahrheit für die Assistenten) |
| `prompts/` | Systemprompts der drei Assistenten |
| `decks/` | Fertige Decks mit Datum, Kaufliste und Spielleitfaden |

Die Sammlungs-CSV (Export aus NocoDB) liegt NICHT hier, sondern wird pro Chat angehängt.

## Regeln für Änderungen

- Die Assistenten haben nur Leserechte. Änderungsvorschläge werden als Text ausgegeben und vom Nutzer eingetragen.
- Jede Datei in `wissen/` trägt oben ein Stand-Datum.
- Bei neuem Set oder neuer Bannliste: `02_format.md`, `03_kartenpool.csv` aktualisieren und Kontrolltest (20 Fragen) wiederholen.

## Status

| Datei | Status |
|---|---|
| wissen/01_regeln_core_2026-10-09.pdf | FEHLT – aus Rules Hub hochladen |
| wissen/01_regeln_turnier_2026-10-09.pdf | FEHLT – aus Rules Hub hochladen |
| wissen/02_format.md | Entwurf, Deckbauregeln noch [BITTE PRÜFEN] |
| wissen/03_kartenpool.csv | nur Kopfzeile |
| wissen/04_meta_turniere.csv | nur Kopfzeile |
| wissen/05_meta_decklisten.md | Vorlage |
| wissen/06_lokale_meta.md | Vorlage (ab Phase 5) |
| prompts/*.md | Entwurf v0.1 |

## Änderungsprotokoll

- 2026-11-07: Grundstruktur angelegt.
