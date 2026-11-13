# Bestandsübersicht Legenden

**Bestandsdatum:** 2026-11-13  
**Quelldateien:** `Riftbound - Karten (Karten) 2026-11-09_18-40.csv`, `03_kartenpool.csv`, `02_format.md`

## Methode und Regelgrundlage

Sammlungszeilen wurden per Setcode und normalisierter Kartennummer (führende Nullen und Alternate-Art-Suffix berücksichtigt) eindeutig `03_kartenpool.csv` zugeordnet; Mehrfachtreffer wurden anhand des Kartentyps aufgelöst. Die Sammlung enthält 468 zugeordnete Zeilen und keine offenen Zuordnungen. Besitz mehrerer Drucke wird je Kartenpool-Kartenname summiert.

Abschnitt 3 zählt ausschließlich besessene Unit-, Spell- und Gear-Namen aus OGS, OGN, SFD, UNL, VEN/Ven und RAD; Legends, Runes und Battlefields sind keine Main-Deck-Karten. Die Bannliste „Offizielle Bannliste Standard Constructed“ aus `02_format.md` ist ausgeschlossen. Die Domänenspalte des Kartenpools wurde als Slash-getrennte Liste gelesen (z. B. `Fury / Order` = beide Domänen). Eine Karte zählt nur, wenn **alle** ihre Domänen in der Identität der Legende liegen. Domainlose/farblose Karten (`Colorless`) würden für alle Identitäten zählen und in der letzten Spalte als Zahl verschiedener Namen ausgewiesen; laut Auswertung gibt es jedoch **0 besessene domainlose/farblose Main-Deck-Kartennamen**. „Kopien roh“ summiert Besitz über Drucke; „Kopien (max 3/Name)“ summiert je Kartenname höchstens drei. Bannliste und Regeldefinitionen stammen aus `02_format.md`.

Plausibilitätsprüfung des gesamten legalen, besessenen Main-Deck-Pools: **384 verschiedene Namen** und **1.250 Kopien roh**; je Einzeldomäne Body 62, Calm 65, Chaos 62, Fury 62, Mind 62 und Order 63; zusätzlich 8 Mehrdomänen-Namen und **0** domainlose/farblose Namen. Die Einzeldomänenzählung ist disjunkt; Mehrdomänenkarten werden separat gezählt. Die Größenordnung von rund 124–130 Namen je Legende (je etwa 62–65 Einzeldomänennamen plus zulässige Mehrdomänenkarten) ist mit zwei Domänen pro Identität vereinbar; sie wurde nicht durch ein fehlerhaftes Trennzeichenparsing erzeugt.

Chosen-Champion-Regel (wörtlich aus `02_format.md`):
> - **Chosen Champion:** Eine Champion Unit mit Champion Tag passend zum Tag der Champion Legend. Sie zählt als eine der genau 40 Main-Deck-Karten (Constructed), obwohl sie zu Spielbeginn in der Champion Zone liegt; sie unterliegt dem Kopienlimit. (CR 103.3, 103.3.a.1–103.3.a.2, 103.3.b.1; TR 402.1)

Domänenidentität (wörtlich aus `02_format.md`):
> - **Domain restrictions:** Karten müssen der Domain Identity entsprechen. Eine Karte mit einer Domain benötigt diese Domain, mit mehreren Domains alle angegebenen Domains; domainlose Karten sind für jede Domain Identity zulässig. (CR 103.2.b.1–103.2.b.5; CR 103.3.c)

Sets (wörtlich aus `02_format.md`):
> - Current Standard laut Tournament Rules: Origins supplemental set contained in Proving Grounds (OGS), Origins (OGN), Spiritforged (SFD), Unleashed (UNL), Vendetta (Ven) und Radiance (RAD). (TR 601.3.c.1–TR 601.3.c.6)

Kopienlimit (wörtlich aus `02_format.md`):
> - **Kopienlimit:** bis zu 3 Exemplare je gleicher Kartenname im Main Deck; das Chosen Champion zählt mit. In Constructed gilt das Limit für die Kombination aus Main Deck und Sideboard. (CR 103.3.b–103.3.b.1; TR 403.3, 601.1.c.3)

## Besessene Legenden

| Legende | Set/Nummer | Domänen | Anzahl im Besitz | Legendentext (Kartenpool) |
|---|---|---|---:|---|
| Azir, Emperor of the Sands | SFD/197 | Calm / Order | 1 | „Your Sand Soldiers have [Weaponmaster].<br>:rb_energy_1:, :rb_exhaust:: Play a 2 :rb_might: Sand Soldier unit token to your base. Use only if you've played an Equipment this turn.“ |
| Diana, Scorn of the Moon | UNL/197 | Mind / Chaos | 4 | „[Reaction][>] :rb_exhaust:: [Add] :rb_energy_1:. Spend this Energy only during showdowns. (Abilities that add resources can't be reacted to.)“ |
| Diana, Scorn of the Moon | UNL/234 | Mind / Chaos | 1 | „[Reaction][>] :rb_exhaust:: [Add] :rb_energy_1:. Spend this Energy only during showdowns.“ |
| Draven, Glorious Executioner | SFD/185 | Fury / Chaos | 1 | „When you win a combat, draw 1. (You win if only your units remain after combat.)“ |
| Ezreal, Prodigal Explorer | SFD/199 | Mind / Chaos | 1 | „:rb_exhaust:: [Reaction] — Draw 1. Use only if you've chosen enemy units and/or gear twice this turn with spells or unit abilities.“ |
| Fiora, Grand Duelist | SFD/205 | Body / Order | 3 | „When one of your units becomes [Mighty], you may exhaust me to channel 1 rune exhausted. (A unit is Mighty while it has 5+ :rb_might:.)“ |
| Irelia, Blade Dancer | SFD/195 | Calm / Chaos | 2 | „When you choose a friendly unit, you may exhaust me and pay :rb_rune_rainbow: to ready it.<br>When you conquer, you may pay :rb_energy_1: to ready me.“ |
| Ivern, Green Father | UNL/195 | Calm / Order | 2 | „When you conquer or hold, you may exhaust me to replace that battlefield with a Brush battlefield token. (Bird, Cat, Dog, Poro, and Ivern units have +1 :rb_might: in Brush. It can be swapped back when scored.)“ |
| Jhin, Virtuoso | UNL/181 | Fury / Mind | 4 | „When you play a spell, if you spent :rb_energy_4: or more, you may banish it. Then, if there are four spells banished with me, put each in its trash, channel 4 runes, and draw 1.“ |
| Kennen, Heart of the Tempest | VEN/155 | Order / Chaos | 2 | „When you play a card from anywhere other than your hand, empower me.<br>[Action][>] Disempower me, :rb_exhaust:: Give a unit [Assault 2] this turn. (+2 :rb_might: while it's an attacker.)“ |
| Kha'Zix, Voidreaver | UNL/201 | Body / Chaos | 3 | „When you win a combat, gain 1 XP.<br>Spend 1 XP, :rb_exhaust:: [Buff] a unit.<br>Spend 2 XP, :rb_exhaust:: Move an exhausted friendly unit from a battlefield to its base.“ |
| LeBlanc, Deceiver | UNL/199 | Mind / Order | 3 | „When you conquer or hold, you may discard 1 and exhaust me to play a ready Reflection unit token there. It becomes a copy of another unit there. Give it [Temporary].“ |
| Lillia, Bashful Bloom | UNL/189 | Calm / Mind | 2 | „:rb_energy_4:, :rb_exhaust:: Play a ready 3 :rb_might: Sprite unit token with [Temporary]. This ability costs :rb_energy_1: less for each friendly unit with [Temporary].“ |
| Lucian, Purifier | SFD/183 | Fury / Body | 3 | „Your Equipment each give [Assault]. (+1 :rb_might: while equipped unit is an attacker.)“ |
| Master Yi, Wuju Master | UNL/191 | Calm / Body | 1 | „[Level 6][>] Your units have +1 :rb_might:. (While you have 6+ XP, get the effect.)<br>[Level 11][>] Your units enter ready.“ |
| Ornn, Fire Below the Mountain | SFD/189 | Calm / Mind | 2 | „:rb_exhaust:: [Reaction] — [Add] :rb_rune_rainbow:. Use only to play gear or use gear abilities. (Abilities that add resources can't be reacted to.)“ |
| Poppy, Keeper of the Hammer | UNL/203 | Body / Order | 4 | „When you hold, gain 1 XP.<br>Spend 3 XP, :rb_exhaust:: Draw 1.“ |
| Pyke, Bloodharbor Ripper | UNL/185 | Fury / Chaos | 4 | „:rb_energy_1:, :rb_exhaust:: Return a friendly unit at a battlefield to its owner's hand. Play a Gold gear token exhausted. (It has "[Reaction][>] Kill this, :rb_exhaust:: [Add] :rb_rune_rainbow:. ")“ |
| Rek'sai, Void Burrower | SFD/187 | Fury / Order | 2 | „When you conquer, you may exhaust me to reveal the top 2 cards of your Main Deck. You may play one. Then recycle the rest.“ |
| Renata Glasc, Chem-Baroness | SFD/201 | Mind / Order | 1 | „When you or an ally hold, you may exhaust me to play a Gold gear token exhausted.<br>While your score is within 3 points of the Victory Score, your Gold [Add] an additional :rb_energy_1:.“ |
| Rengar, Pridestalker | UNL/183 | Fury / Body | 2 | „When you play a unit, give a unit +1 :rb_might: this turn.“ |
| Rumble, Mechanized Menace | SFD/181 | Fury / Mind | 1 | „Your Mechs have [Shield]. (+1 :rb_might: while they're defenders.)“ |
| Sivir, Battle Mistress | SFD/203 | Body / Chaos | 1 | „When you recycle a rune, you may exhaust me to play a Gold gear token exhausted.<br>When one or more enemy units die, ready me.“ |
| Vex, Gloomist | UNL/193 | Calm / Chaos | 2 | „When you or an ally hold, you may exhaust me to draw 1.“ |
| Vi, Piltover Enforcer | UNL/187 | Fury / Order | 2 | „When you conquer, if you assigned 3 or more excess damage, you may exhaust me to ready a unit.“ |

## Champions im Besitz nach Legende

### Diana, Scorn of the Moon (UNL/234)

- Diana, Lunari (UNL/79): 2 Kopie(n). Kartentext (03_kartenpool.csv): „When a showdown begins here, you may pay :rb_energy_1:. If you do, [Predict], then reveal the top card of your Main Deck. If it's a spell, draw it. (To Predict, look at the top card of your Main Deck. You may recycle it.)“

### Irelia, Blade Dancer (SFD/195)

- Irelia, Fervent (SFD/57): 2 Kopie(n). Kartentext (03_kartenpool.csv): „[Deflect] (Opponents must pay :rb_rune_rainbow: to choose me with a spell or ability.)
When you choose or ready me, give me +1 :rb_might: this turn.“
- Irelia, Graceful (SFD/141): 1 Kopie(n). Kartentext (03_kartenpool.csv): „Your spells that choose me cost :rb_energy_1: or :rb_rune_rainbow: less.“

### Azir, Emperor of the Sands (SFD/197)

- Azir, Ascendant (SFD/50): 1 Kopie(n). Kartentext (03_kartenpool.csv): „:rb_rune_calm:: [Action] — Choose a unit you control. Move me to its location and it to my original location. If it's equipped, you may attach one of its Equipment to me. Use only once per turn.“

### Lillia, Bashful Bloom (UNL/189)

- Lillia, Fae Fawn (UNL/82): 2 Kopie(n). Kartentext (03_kartenpool.csv): „[Accelerate] (You may pay :rb_energy_1::rb_rune_mind: as an additional cost to have me enter ready.)
When I move from a location, play a 3 :rb_might: Sprite unit token with [Temporary] there. (Kill it at the start of its controller's Beginning Phase, before scoring.)“
- Lillia, Protector of Dreams (UNL/58): 1 Kopie(n). Kartentext (03_kartenpool.csv): „When you play a token unit, give me +1 :rb_might: this turn.
Your token units have [Tank]. (They must be assigned combat damage first.)“

### Draven, Glorious Executioner (SFD/185)

- Draven, Audacious (SFD/148): 1 Kopie(n). Kartentext (03_kartenpool.csv): „[Deflect] (Opponents must pay :rb_rune_rainbow: to choose me with a spell or ability.)
The first time I win a combat each turn, you score 1 point.
When I die in combat, choose an opponent. They score 1 point.“

### Diana, Scorn of the Moon (UNL/197)

- Diana, Lunari (UNL/79): 2 Kopie(n). Kartentext (03_kartenpool.csv): „When a showdown begins here, you may pay :rb_energy_1:. If you do, [Predict], then reveal the top card of your Main Deck. If it's a spell, draw it. (To Predict, look at the top card of your Main Deck. You may recycle it.)“

### LeBlanc, Deceiver (UNL/199)

- LeBlanc, Fragmented (UNL/172): 2 Kopie(n). Kartentext (03_kartenpool.csv): „[Assault] (+1 :rb_might: while I'm an attacker.)
[Deathknell][>] Draw 1. If it's your Beginning Phase, draw 2 instead. (When I die, get the effect.)“

### Ornn, Fire Below the Mountain (SFD/189)

- Ornn, Forge God (SFD/85): 1 Kopie(n). Kartentext (03_kartenpool.csv): „[Deflect 2] (Opponents must pay :rb_rune_rainbow::rb_rune_rainbow: to choose me with a spell or ability.)
[Weaponmaster] (When you play me, you may [Equip] one of your Equipment to me for :rb_rune_rainbow: less, even if it's already attached.)
I have +1 :rb_might: for each friendly gear.“

### Master Yi, Wuju Master (UNL/191)

- Master Yi, Tempered (UNL/113): 4 Kopie(n). Kartentext (03_kartenpool.csv): „[Hunt 2] (When I conquer or hold, gain 2 XP.)
[Level 6][>] I have [Deflect] and [Ganking]. (While you have 6+ XP, opponents must pay :rb_rune_rainbow: to choose me with a spell or ability and I can move from battlefield to battlefield.)“

### Rek'sai, Void Burrower (SFD/187)

- Rek'Sai, Swarm Queen (SFD/170): 1 Kopie(n). Kartentext (03_kartenpool.csv): „When I attack, you may reveal the top 2 cards of your Main Deck. You may play one. Then recycle the rest. If the played card is a unit, you may play it here.“

### Sivir, Battle Mistress (SFD/203)

- Sivir, Mercenary (SFD/143): 1 Kopie(n). Kartentext (03_kartenpool.csv): „[Accelerate] (You may pay :rb_energy_1::rb_rune_chaos: as an additional cost to have me enter ready.)
If you've spent at least :rb_rune_rainbow::rb_rune_rainbow: this turn, I have +2 :rb_might: and [Ganking]. (I can move from battlefield to battlefield.)“

### Poppy, Keeper of the Hammer (UNL/203)

- Poppy, Paragon (UNL/116): 2 Kopie(n). Kartentext (03_kartenpool.csv): „[Deflect] (Opponents must pay :rb_rune_rainbow: to choose me with a spell or ability.)
When you play me, if an opponent's score is within 3 points of the Victory Score, ready me and gain 3 XP.“

### Lucian, Purifier (SFD/183)

- Lucian, Merciless (SFD/113): 1 Kopie(n). Kartentext (03_kartenpool.csv): „[Weaponmaster] (When you play me, you may [Equip] one of your Equipment to me for :rb_rune_rainbow: less, even if it's already attached.)
The first time I conquer each turn, ready me.“

### Fiora, Grand Duelist (SFD/205)

- Fiora, Peerless (SFD/110): 1 Kopie(n). Kartentext (03_kartenpool.csv): „When I attack or defend one on one, double my Might this combat.“

### Renata Glasc, Chem-Baroness (SFD/201)

- Renata Glasc, Industrialist (SFD/171): 2 Kopie(n). Kartentext (03_kartenpool.csv): „Your tokens enter ready.“

### Ezreal, Prodigal Explorer (SFD/199)

- kein Champion im Besitz.

### Pyke, Bloodharbor Ripper (UNL/185)

- Pyke, Dockside Butcher (UNL/28): 2 Kopie(n). Kartentext (03_kartenpool.csv): „[Hidden] (Hide now for :rb_rune_rainbow: to react with later for :rb_energy_0:.)
[Ganking] (I can move from battlefield to battlefield.)
You may pay :rb_rune_fury: as an additional cost to play me.
When you play me, if you paid the additional cost, ready me and give me +2 :rb_might: this turn.“
- Pyke, Returned (UNL/145): 1 Kopie(n). Kartentext (03_kartenpool.csv): „[Hidden] (Hide now for :rb_rune_rainbow: to react with later for :rb_energy_0:.)
[Backline] (I must be assigned combat damage last.)
Once each turn, when an enemy unit dies while I'm at a battlefield, play a Gold gear token exhausted. (It has "[Reaction][>] Kill this, :rb_exhaust:: [Add] :rb_rune_rainbow:. ")“

### Rengar, Pridestalker (UNL/183)

- Rengar, Pouncing (SFD/25): 2 Kopie(n). Kartentext (03_kartenpool.csv): „[Reaction] (Play any time, even before spells and abilities resolve, including to a battlefield you control.)
[Assault 2] (+2 :rb_might: while I'm an attacker.)
I can be played to a battlefield you're attacking.“
- Rengar, Unseen (UNL/24): 1 Kopie(n). Kartentext (03_kartenpool.csv): „[Accelerate] (You may pay :rb_energy_1::rb_rune_fury: as an additional cost to have me enter ready.)
[Assault 2] (+2 :rb_might: while I'm an attacker.)
[Deflect] (Opponents must pay :rb_rune_rainbow: to choose me with a spell or ability.)
[Ganking] (I can move from battlefield to battlefield.)"

### Jhin, Virtuoso (UNL/181)

- Jhin, Murderous Artist (UNL/22): 3 Kopie(n). Kartentext (03_kartenpool.csv): „[Deflect] (Opponents must pay :rb_rune_rainbow: to choose me with a spell or ability.)
[Ganking] (I can move from battlefield to battlefield.)
When I move, [Add] :rb_energy_1::rb_rune_rainbow:. (Abilities that add resources can't be reacted to.)“

### Ivern, Green Father (UNL/195)

- Ivern, Verdant Caretaker (UNL/1): 1 Kopie(n). Kartentext (03_kartenpool.csv): „[Assault] (+1 :rb_might: while I'm an attacker.)
[Deflect] (Opponents must pay :rb_rune_rainbow: to choose me with a spell or ability.)“

### Vi, Piltover Enforcer (UNL/187)

- Vi, Vaultbreaker (UNL/146): 1 Kopie(n). Kartentext (03_kartenpool.csv): „[Assault] (+1 :rb_might: while I'm an attacker.)
[Deflect] (Opponents must pay :rb_rune_rainbow: to choose me with a spell or ability.)
[Hunt 2] (When I conquer or hold, gain 2 XP.)“

### Kennen, Heart of the Tempest (VEN/155)

- Kennen, Keeper of Balance (VEN/135): 2 Kopie(n). Kartentext (03_kartenpool.csv): „[Hidden] (Hide now for :rb_rune_rainbow: to react with later for :rb_energy_0:.)
When you play me or I attack, you may pay :rb_energy_2: to [Stun] a unit. (It doesn't deal combat damage this turn.)
While there's a stunned enemy unit here, I have +2 :rb_might:.“

### Vex, Gloomist (UNL/193)

- Vex, Mocking (UNL/55): 1 Kopie(n). Kartentext (03_kartenpool.csv): „[Shield] (+1 :rb_might: while I'm a defender.)
[Tank] (I must be assigned combat damage first.)
When you [Stun] an enemy unit at a battlefield, you may move me to that battlefield.“

### Rumble, Mechanized Menace (SFD/181)

- Rumble, Hotheaded (SFD/26): 1 Kopie(n). Kartentext (03_kartenpool.csv): „Your Mechs each have [Assault]. (+1 :rb_might: while we're attackers.)
When I conquer, you may recycle another friendly unit to play a Mech from your trash. Reduce its Energy cost by the Might of the unit you recycled.“

### Kha'Zix, Voidreaver (UNL/201)

- Kha'Zix, Mutating Horror (UNL/143): 4 Kopie(n). Kartentext (03_kartenpool.csv): „[Ambush] (You may play me as a [Reaction] to a battlefield where you have units.)
When I attack or defend, if an enemy unit is alone here, give me +2 :rb_might: this turn and gain 2 XP.“

## Main-Deck-Bestand nach Legenden

| Legende | Domänen | verschiedene Namen | Kopien roh | Kopien (max 3/Name) | davon domänenlos (Namen) |
|---|---|---:|---:|---:|---:|
| Diana, Scorn of the Moon (UNL/234) | Mind / Chaos | 125 | 409 | 251 | 0 |
| Irelia, Blade Dancer (SFD/195) | Calm / Chaos | 127 | 406 | 256 | 0 |
| Azir, Emperor of the Sands (SFD/197) | Calm / Order | 130 | 418 | 269 | 0 |
| Lillia, Bashful Bloom (UNL/189) | Calm / Mind | 127 | 403 | 255 | 0 |
| Draven, Glorious Executioner (SFD/185) | Fury / Chaos | 124 | 417 | 253 | 0 |
| Diana, Scorn of the Moon (UNL/197) | Mind / Chaos | 125 | 409 | 251 | 0 |
| LeBlanc, Deceiver (UNL/199) | Mind / Order | 127 | 418 | 261 | 0 |
| Ornn, Fire Below the Mountain (SFD/189) | Calm / Mind | 127 | 403 | 255 | 0 |
| Master Yi, Wuju Master (UNL/191) | Calm / Body | 127 | 407 | 256 | 0 |
| Rek'sai, Void Burrower (SFD/187) | Fury / Order | 127 | 428 | 265 | 0 |
| Sivir, Battle Mistress (SFD/203) | Body / Chaos | 125 | 412 | 251 | 0 |
| Poppy, Keeper of the Hammer (UNL/203) | Body / Order | 125 | 420 | 260 | 0 |
| Lucian, Purifier (SFD/183) | Fury / Body | 124 | 418 | 253 | 0 |
| Fiora, Grand Duelist (SFD/205) | Body / Order | 125 | 420 | 260 | 0 |
| Renata Glasc, Chem-Baroness (SFD/201) | Mind / Order | 127 | 418 | 261 | 0 |
| Ezreal, Prodigal Explorer (SFD/199) | Mind / Chaos | 125 | 409 | 251 | 0 |
| Pyke, Bloodharbor Ripper (UNL/185) | Fury / Chaos | 124 | 417 | 253 | 0 |
| Rengar, Pridestalker (UNL/183) | Fury / Body | 124 | 418 | 253 | 0 |
| Jhin, Virtuoso (UNL/181) | Fury / Mind | 124 | 414 | 252 | 0 |
| Ivern, Green Father (UNL/195) | Calm / Order | 130 | 418 | 269 | 0 |
| Vi, Piltover Enforcer (UNL/187) | Fury / Order | 127 | 428 | 265 | 0 |
| Kennen, Heart of the Tempest (VEN/155) | Order / Chaos | 125 | 419 | 260 | 0 |
| Vex, Gloomist (UNL/193) | Calm / Chaos | 127 | 406 | 256 | 0 |
| Rumble, Mechanized Menace (SFD/181) | Fury / Mind | 124 | 414 | 252 | 0 |
| Kha'Zix, Voidreaver (UNL/201) | Body / Chaos | 125 | 412 | 251 | 0 |

Laut Auswertung gibt es **0 besessene domainlose/farblose Main-Deck-Kartennamen**; entsprechend steht in der letzten Spalte für jede Legende 0.

## Battlefields im Besitz

| Battlefield | Set/Nummer | Anzahl im Besitz | Status |
|---|---|---:|---|
| Sunken Temple | SFD/218 | 2 | legaler Setpool |
| Rockfall Path | SFD/216 | 2 | legaler Setpool |
| Ravenbloom Conservatory | SFD/215 | 1 | legaler Setpool |
| Seat of Power | SFD/217 | 1 | legaler Setpool |
| Star Spring | UNL/215 | 8 | legaler Setpool |
| Ornn's Forge | SFD/213 | 1 | legaler Setpool |
| Forbidding Waste | UNL/210 | 5 | legaler Setpool |
| Abandoned Hall | UNL/205 | 7 | legaler Setpool |
| Emperor's Dais | SFD/207 | 1 | legaler Setpool |
| Minefield | SFD/212 | 1 | legaler Setpool |
| Dusk Rose Lab | UNL/209 | 8 | legaler Setpool |
| Hall of Legends | SFD/210 | 1 | legaler Setpool |
| Treasure Hoard | SFD/220 | 2 | legaler Setpool |
| Forgotten Monument | SFD/209 | 1 | legaler Setpool |
| Veiled Temple | SFD/221 | 2 | legaler Setpool |
| Frozen Fortress | UNL/212 | 4 | legaler Setpool |
| Power Nexus | SFD/214 | 4 | legaler Setpool |
| Black Flame Altar | UNL/208 | 3 | legaler Setpool |
| The Papertree | SFD/219 | 1 | legaler Setpool |
| Marai Spire | SFD/211 | 1 | legaler Setpool |
| Dragon Roost | VEN/157 | 3 | legaler Setpool |
| Valley of Idols | UNL/218 | 6 | legaler Setpool |
| Vaults of Helia | UNL/219 | 4 | legaler Setpool |
| Altar of Blood | UNL/206 | 10 | legaler Setpool |
| Gardens of Becoming | UNL/213 | 8 | legaler Setpool |
| Ripper's Bay | UNL/214 | 6 | legaler Setpool |
| The Academy | UNL/216 | 5 | legaler Setpool |
| Amateur Recital | UNL/207 | 5 | legaler Setpool |
| Trapping Grounds | UNL/217 | 8 | legaler Setpool |
| Forgotten Library | UNL/211 | 3 | legaler Setpool |

## Nicht zuordenbare Karten [BITTE PRÜFEN]

- Keine. Alle besessenen Sammlungskarten wurden eindeutig zugeordnet.

## Prüfhinweise

- Kartenpool-Zuordnungen: 468 (Set/Nummer oder eindeutiger Fallback); nicht zugeordnet: 0.
- Der Sammlungsname **Bushwack** (SFD/4) wurde per Set und Nummer eindeutig dem Kartenpooleintrag **Bushwhack** (SFD/4, Spell, Fury) zugeordnet; die Typübereinstimmung bestätigt die Zuordnung.
- `02_format.md` Zeile 13: weitergehende Rotationsplanung [BITTE PRÜFEN].
