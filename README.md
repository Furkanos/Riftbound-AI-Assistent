# Riftbound-AI-Assistent

Lokaler Deckbau und Deckcheck für Riftbound. Einstieg: [Workflow-Anleitung](ANLEITUNG_WORKFLOW.md). Die vier Assistentenrollen stehen unter `prompts/`.

## Was bleibt lokal?

Eigene Decks, Inventar- und Katalogexporte, der Kartenpool, generierte Sammlungsdaten und `ergebnis/`. Ein frischer Clone enthält diese Dateien nicht. `decks/VORLAGE.csv` bleibt als Vorlage im Repo.

## Zwei getrennte Prüfwege

| Weg | Eingabe | Ergebnis |
|---|---|---|
| Lokaler Deckcheck | Eigene Deck-CSV und, für den Vollcheck, lokale Daten | Berichte unter `ergebnis/`, abhängig von den Eingaben |
| GitHub Actions | Synthetische Test-CSV ohne Inventar | Strukturbericht als Artefakt; kein Commit und kein Push durch den Workflow |

## Welche Quelle entscheidet?

1. **Regeln, Kartentexte, Banns und Set-Freigaben:** offizielle Riot-Quellen, siehe [Quellenübersicht](quellen.md). Ohne aktuellen Abgleich keine Turnierfreigabe.
2. **Besitz und lokale Vorauswahl:** Das Inventar belegt Besitz, der Kartenpool nicht. Lokale Snapshots belegen keinen aktuellen Bann- oder Set-Stand.
3. **Strategie und Meta:** datierte Turnierbelege und nachvollziehbare Heuristiken. Empfehlungen sind keine Regelentscheidungen.
