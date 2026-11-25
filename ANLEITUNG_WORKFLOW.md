# Workflow: Deck bauen und prüfen

## 1. Deck lokal anlegen

Kopiere `decks/VORLAGE.csv` nach `decks/mein_deck.csv` und ersetze die Beispielzeilen. Der Kopf lautet `Anzahl;Name;Set;Nummer;Bereich`. Verwende nach Möglichkeit Set und Kartennummer. Bereiche: `Legende`, `Champion`, `Main`, `Battlefield`, `Rune`, `Sideboard`. Eine eigene Zeile mit `# UNVOLLSTÄNDIG` kennzeichnet eine Teilliste.

Die eigene Deck-CSV bleibt lokal. Nicht auf GitHub hochladen oder mit `git add -f` erzwingen.

## 2. Lokale Daten und Berichte erzeugen

Lege Inventar- und Katalogexport sowie `wissen/03_kartenpool.csv` lokal unter `wissen/` ab. `wissen/02_format.md` ist eine Arbeitsreferenz, keine Live-Freigabe.

Im Repo-Stamm ausführen:

```sh
python3 tools/datenbasis.py
python3 tools/deckcheck.py
python3 tools/deckqualitaet.py
```

- `datenbasis.py` erzeugt die normalisierte Sammlung, Kartentags und eine Liste offener Zuordnungen.
- `deckcheck.py` schreibt Berichte nach `ergebnis/`. Besitz-, Einkaufs-, Kartentext- und Alternativenberichte hängen von den verfügbaren Eingaben ab. Fehlende Preisangaben bedeuten nicht kostenlos. Runen gelten beim Besitzabgleich als unbegrenzt.
- `deckqualitaet.py` erzeugt eine strategische Qualitätsauswertung, keine Legalitätsfreigabe.

Für einen reinen CSV-Strukturcheck ohne Inventar: `python3 tools/deckcheck.py --structure-only`. Ein Strukturbericht ersetzt keinen Vollcheck. `Legal=ja` in der lokalen Datenbasis ist eine Vorauswahl, keine aktuelle Turnierfreigabe. Bannstatus und Set-Freigabe separat anhand der offiziellen Quellen in [quellen.md](quellen.md) prüfen. Ohne Abgleich: `NICHT VERIFIZIERT`.

## 3. Deckbau und Pflege

Nutze `daten/legenden_engine.csv` für Engine-Zuordnungen. Prüfe automatische Tags am Kartentext. Gleiche Domänen, verfügbare Kopien und offene Zuordnungen ab. Als Startwerte, nicht als Regeln: mindestens 14 Engine-Karten, mindestens 12 Einheiten mit Kosten bis 3 und mindestens 6 Removal-Karten. Passe diese Ziele an den Archetyp an. Notiere fürs Sideboard je Matchup einen Rein/Raus-Plan mit Begründung.

Prüfe offene Zuordnungen in `daten/zuordnung_offen.csv`. Pflege bestätigte Namensvarianten in `daten/namens_alias.csv` und Tag-Korrekturen mit Beleg in `daten/tags_manuell.csv`, nicht in den generierten CSVs.

Pflege Meta-Berichte mit Datum und Belegen. Baue gegen das belegte Feld, statt Toplisten ungeprüft zu kopieren.

## 4. GitHub Actions prüfen

Der Workflow `Deckcheck` läuft bei passenden Pushes und Pull Requests oder per manuellem Start. Er erzeugt eine synthetische Test-CSV und prüft sie mit `--structure-only`. Der Strukturbericht liegt als Artefakt im jeweiligen Lauf unter **Actions → Deckcheck**, nicht als Datei im Repository.

CI prüft weder private Decks noch Besitz oder aktuelle Turnierlegalität. Der Workflow braucht keine Schreibrechte auf Repository-Inhalte.
