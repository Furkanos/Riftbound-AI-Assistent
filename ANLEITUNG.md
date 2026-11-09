# Neues Deck prüfen in 3 Klicks

## 1. Deckdatei anlegen
Im Repository `decks/` die Datei `VORLAGE.csv` kopieren, z. B. als `decks/mein-deck.csv`. CSV-Trennzeichen ist Semikolon; Überschrift und Beispiel:

```csv
Bereich;Anzahl;Name;Set;Nummer
Legende;1;Kai'Sa, Daughter of the Void;OGN;247
Champion;1;Kai'Sa, Survivor;OGN;39
Main;3;Beispielkarte;OGN;1
Rune;12;Fury Rune;OGN;7
Battlefield;1;Beispiel-Schlachtfeld;OGN;1
Sideboard;1;Beispielkarte;OGN;1
```

Zulässige Bereiche: Legende, Champion, Main, Rune/Runen, Battlefield/Battlefields und Sideboard. Verwende pro Zeile Kartenname und nach Möglichkeit Set und Nummer aus dem Katalog. Schreibe `# UNVOLLSTÄNDIG` in eine eigene Zeile ganz oben, wenn die Liste nicht vollständig bestätigt ist. Unbekannte Karten erscheinen als Fehler und führen zu NICHT BESTANDEN; sie werden nicht verworfen.

## 2. Datei hochladen
Auf GitHub im Ordner `decks/` wähle **Add file → Upload files**, lade die CSV hoch und bestätige mit **Commit changes**.

## 3. Ergebnis ansehen
Öffne **Actions → Deckcheck**, den neuesten Lauf und nach Abschluss den Repository-Ordner `ergebnis/`. Dort liegen `<name>_legalitaet.md`, `<name>_deckcheck.csv` und `<name>_kaufliste.csv`. Preise, die im Inventar nicht vorhanden sind, werden als **PREIS FEHLT** angezeigt. Der Workflow läuft auch manuell über **Actions → Deckcheck → Run workflow**.

Falls der Workflow Ergebnisse nicht committen darf: **Settings → Actions → General → Workflow permissions → Read and write permissions → Save**. (Die Workflow-Datei gewährt zusätzlich `contents: write`.)
