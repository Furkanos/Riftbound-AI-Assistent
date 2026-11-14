# Deckbau-Ablauf (verbindlich für jeden Prompt „Baue Deck X“)

## Quellen – nur diese benutzen
1. `daten/sammlung_normalisiert.csv` – Pool. Nur Zeilen mit `Legal=ja`, Domäne ⊆ Legenden-Domänen, höchstens `Spielbar` Kopien.
2. `daten/karten_tags.csv` – Rollen. `Quelle=manuell` ist geprüft, `auto` ist Entwurf: vor Verwendung als Engine-Karte den `Text` lesen.
3. `daten/legenden_engine.csv` – welcher Tag die Legende auslöst.
4. `wissen/regeln_auszug.md` – Regeln. Die 514-KB-Datei nur bei neuer Regelfrage durchsuchen und die Stelle danach hier ergänzen.
5. `wissen/meta_bedrohungen.md` – wogegen gebaut wird.
Nicht neu zuordnen, nicht neu taggen, keine Zählweise erfinden.

## Bauen
1. Chosen Champion 1× (Bereich Champion), weitere Kopien bis Spielbar im Main.
2. Engine: so viele Karten mit dem Engine-Tag wie sinnvoll, Ziel ≥ 14.
3. Kurve: Ziel ≥ 12 Einheiten mit Kosten ≤ 3.
4. Interaktion: ≥ 6 removal; gear_antwort laut meta_bedrohungen.md.
5. Rest: Finisher (2–4) und Karten ziehen.
6. Sideboard ≤ 10 mit 1:1-Plan je Tier-Deck (Rein/Raus/Grund mit Kartentext-Zitat).
7. Jede genannte Karte mit Zitat aus der Spalte `Text`.

## Prüfen
Speichern als `decks/<legende>_vN.csv` (Format siehe ANLEITUNG.md). Warten, bis der Workflow `ergebnis/<name>_legalitaet.md` und `ergebnis/<name>_qualitaet.md` erzeugt hat. Nur deren Zahlen berichten. Bei NICHT BESTANDEN oder Zielwert verfehlt: korrigieren und neu speichern. Keine Kopfrechnung; Unklares als [BITTE PRÜFEN].

## Pflege (nur du)
- `daten/zuordnung_offen.csv` ansehen → gleiche Karte unter anderem Namen in `daten/namens_alias.csv` eintragen.
- Falsche/fehlende Tags in `daten/tags_manuell.csv` (Wert 1 = setzen, 0 = entfernen, Beleg = Zitat).
- Neuer Meta-Bericht → `wissen/meta_bedrohungen.md` anpassen.

## Beispiel-Prompts
- „Baue ein Deck für Master Yi nach ANLEITUNG_DECKBAU.md.“
- „Vergleiche alle Legenden in daten/legenden_engine.csv per Engine-Tag-Kopien und baue die besten zwei.“
