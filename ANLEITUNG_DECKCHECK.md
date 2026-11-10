# Deckcheck verwenden

1. Kopiere `decks/VORLAGE.csv`, benenne sie beispielsweise in `decks/mein_deck.csv` um und ersetze die Beispieldaten. Die CSV ist mit Semikolon getrennt.
2. Trage Anzahl, Kartenname und möglichst Set + Kartennummer ein. Bereich muss `Legende`, `Champion`, `Main`, `Battlefield`, `Rune` oder `Sideboard` sein. Pro Kartenzeile eine Zeile; Foil/Normal braucht keine Unterscheidung.
3. Speichere die Datei unter `decks/` und committe sie. GitHub Actions erstellt die Berichte unter `ergebnis/` und committet Änderungen zurück. Manuell geht es über Actions → Deckcheck → Run workflow.
4. `ergebnis/mein_deck_deckcheck.csv` zeigt Bedarf, Besitz und Fehlmengen. `ergebnis/mein_deck_legalitaet.md` zeigt die Regelchecks. Leere Kostenfelder bedeuten, dass im Inventar kein Preis bekannt ist, nicht dass die Karte kostenlos ist.
5. Sammlungs- und Katalogdaten liegen unter `wissen/`. Bei Änderungen dieser Daten startet der Check automatisch.

Besitz wird zuerst nach Set + Nummer abgeglichen, sonst über den normalisierten Namen. Eine Kommentarzeile mit `# UNVOLLSTÄNDIG: ...` markiert eine Teildeckliste. Geprüft werden nur Regeln, die in `wissen/02_format.md` festgehalten sind.

Runen gelten immer als unbegrenzt vorhanden; nie als fehlend oder Kaufposten zählen.
