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

- Die Assistenten haben nur Leserechte. Änderungsvorschläge an Dateien werden als Text ausgegeben und vom Nutzer eingetragen.
- Jede Datei in `wissen/` trägt oben ein Stand-Datum.
- Bei neuem Set oder neuer Bannliste: `02_format.md`, `03_kartenpool.csv` aktualisieren und Kontrolltest (20 Fragen) wiederholen.

## Status

| Datei | Status |
|---|---|
| wissen/RiftboundCoreRulesRUP5_En_EN.pdf | Quelldokument vorhanden; Last Updated 2026-10-09 |
| wissen/RiftboundTournamentRulesRUP5_en_EN.pdf | Quelldokument vorhanden; Last Updated 2026-10-09 |
| wissen/01_regeln_core.md | Markdown-Konvertierung erstellt; vollständige lokale Sicherung vorhanden; Repository-Aufteilung ausstehend |
| wissen/01_regeln_turnier.md | Markdown-Konvertierung erstellt; vollständige lokale Sicherung vorhanden; Repository-Aufteilung ausstehend |
| wissen/02_format.md | Deckbau-, Legalitäts-, Sideboard-, Match- und Zeitregeln mit Quellenbelegen; offizielle Bannliste für sanktionierte Constructed-Turniere bestätigt (2026-11-07) |
| wissen/03_kartenpool.csv | erstellt, Stichprobe offen |
| wissen/04_meta_turniere.csv | nur Kopfzeile |
| wissen/05_meta_decklisten.md | Vorlage |
| wissen/06_lokale_meta.md | Vorlage (ab Phase 5) |
| prompts/*.md | Entwurf v0.1 |

## Änderungsprotokoll

- 2026-11-07: Grundstruktur angelegt.
- 2026-11-07: `02_format.md` anhand der Core Rules und Tournament Rules (Last Updated 2026-10-09) um Deckbau-, Format-, Sideboard-, Legalitäts- und Zeitregeln samt Regelnummern ergänzt; offizielle Bannliste für sanktionierte Constructed-Turniere bestätigt und eingetragen.
- 2026-11-07: Vollständige englische Core Rules und Tournament Rules (RUP5; Last Updated 2026-10-09) aus den Quelldokumenten als Markdown übertragen und lokal als Fallback gesichert. Die Aufteilung in kleinere Repository-Dateien samt Indizes ist noch nicht veröffentlicht.
- 2026-11-07: Kartenpool aus Rifthunt-Bulk-Export erstellt; rechtliche Sets und Bannliste abgeglichen; Stichprobe offen.
