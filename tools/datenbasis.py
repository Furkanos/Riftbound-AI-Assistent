#!/usr/bin/env python3
"""Erzeugt die feste Datenbasis (nur Standardbibliothek):
  daten/sammlung_normalisiert.csv  - jede besessene Karte einmal, mit Pool-Daten
  daten/karten_tags.csv            - Rollen je Karte (auto = Entwurf, manuell = geprueft)
  daten/zuordnung_offen.csv        - Inventarzeilen, die NICHT sicher zugeordnet sind
Korrekturen von Hand NUR in daten/namens_alias.csv und daten/tags_manuell.csv.
"""
import csv, re, sys
from collections import defaultdict
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from deckcheck import norm, num, readcsv, dec, pick, LEGAL

ROOT = Path(__file__).resolve().parents[1]
DATEN = ROOT / 'daten'

# Automatische Tag-Regeln (Entwurf). Treffer werden mit Textstelle belegt.
TAG_REGELN = [
    ('removal', r"\b(kill|banish)\b[^.]{0,30}\bunit|\bdeal \d+\b[^.]{0,30}\benemy unit|\[stun\]|\bstun\b[^.]{0,20}\bunit|return an enemy unit"),
    ('gear_antwort', r"\b(kill|banish|destroy|return)\b[^.]{0,20}\bgear\b"),
    ('konter', r"\bcounter\b[^.]{0,25}\bspell"),
    ('xp_quelle', r"\bgain \d+ xp\b|\[hunt"),
    ('nicht_aus_hand', r"\[hidden\]|\bplay\b[^.]{0,40}\bfrom (your|the) (trash|deck|top)|you may play this from"),
    ('equipment', r"\[equip\]"),
    ('waehlt_eigene_einheit', r"\bchoose a (friendly )?unit\b|\ba unit you control\b|\bgive (a|another) (friendly )?unit\b|\bchoose a unit at\b"),
    ('temporary', r"\[temporary\]"),
    ('mech', r"\bmechs?\b"),
    ('karten_ziehen', r"\bdraw \d+|\bdraw a card"),
]


def bannliste():
    fmt = (ROOT / 'wissen/02_format.md').read_text(encoding='utf-8')
    bans, table = set(), False
    for line in fmt.splitlines():
        if 'Bannliste Standard' in line:
            table = True
            continue
        if table and line.startswith('## '):
            break
        if table and line.startswith('- '):
            bans.add(norm(line[2:].strip()))
    return bans


def lade_alias():
    alias = {}
    p = DATEN / 'namens_alias.csv'
    if p.exists():
        for r in readcsv(p):
            a, b = norm(r.get('Inventarname')), norm(r.get('Kartenname'))
            if a and b:
                alias[a] = b
    return alias


def main():
    DATEN.mkdir(exist_ok=True)
    invs = sorted((ROOT / 'wissen').glob('*Karten (Karten)*.csv'))
    if not invs:
        raise SystemExit('Inventar fehlt in wissen/.')
    pool = readcsv(ROOT / 'wissen/03_kartenpool.csv')
    pkey, pname = defaultdict(list), {}
    for r in pool:
        k = (str(r.get('Set') or '').strip().upper(), num(r.get('Nummer')))
        pkey[k].append(r)
        pname.setdefault(norm(r.get('Name')), r)
    alias, bans = lade_alias(), bannliste()

    besitz = defaultdict(int)   # norm(Pool-Name) -> Kopien
    drucke = defaultdict(set)
    poolrow = {}
    offen = []
    for r in readcsv(invs[0]):
        titel = r.get('Titel', '')
        q = int(dec(r.get('Owned')))
        if q <= 0:
            continue
        n = norm(titel)
        n = alias.get(n, n)
        k = (r.get('SetCode', '').strip().upper(), num(r.get('Kartennummer')))
        treffer = next((p for p in pkey.get(k, []) if norm(p.get('Name')) == n), None)
        weg = 'Set+Nummer+Name'
        if treffer is None and n in pname:
            treffer, weg = pname[n], 'Name'
        if treffer is None:
            kand = '; '.join(p.get('Name', '') for p in pkey.get(k, [])) or '-'
            offen.append([titel, k[0], k[1], q, kand,
                          'Name passt nicht zur Nummer: in daten/namens_alias.csv eintragen, falls dieselbe Karte' if kand != '-' else 'nicht im Kartenpool'])
            continue
        pn = norm(treffer.get('Name'))
        besitz[pn] += q
        drucke[pn].add(f"{treffer.get('Set')}-{treffer.get('Nummer')}")
        poolrow.setdefault(pn, treffer)

    zeilen = []
    for pn in sorted(besitz, key=lambda x: poolrow[x].get('Name', '')):
        p = poolrow[pn]
        sets = {d.split('-')[0].upper() for d in drucke[pn]}
        legal = bool(sets & LEGAL) and pn not in bans
        text = pick(p, 'Kartentext', 'Text', anytext=True)
        zeilen.append({
            'Name': p.get('Name', ''), 'Drucke': ' '.join(sorted(drucke[pn])),
            'Typ': pick(p, 'Typ'), 'Domaene': pick(p, 'Domäne', 'Domaene', 'Domänen'),
            'Kosten': pick(p, 'Kosten'), 'Stats': pick(p, 'Stats'),
            'Besitz': besitz[pn], 'Spielbar': min(besitz[pn], 3) if legal else 0,
            'Legal': 'ja' if legal else 'nein', 'Text': text,
        })
    felder = ['Name', 'Drucke', 'Typ', 'Domaene', 'Kosten', 'Stats', 'Besitz', 'Spielbar', 'Legal', 'Text']
    with (DATEN / 'sammlung_normalisiert.csv').open('w', encoding='utf-8-sig', newline='') as f:
        w = csv.DictWriter(f, fieldnames=felder, delimiter=';')
        w.writeheader()
        w.writerows(zeilen)
    with (DATEN / 'zuordnung_offen.csv').open('w', encoding='utf-8-sig', newline='') as f:
        w = csv.writer(f, delimiter=';')
        w.writerow(['Inventarname', 'Set', 'Nummer', 'Besitz', 'Pool-Kandidaten', 'Aktion'])
        w.writerows(offen)

    # Tags: automatisch, dann manuelle Uebersteuerung
    tags = {}
    for z in zeilen:
        t = z['Text'].casefold()
        for tag, rx in TAG_REGELN:
            m = re.search(rx, t)
            if m:
                tags[(norm(z['Name']), tag)] = ('auto', m.group(0))
    mp = DATEN / 'tags_manuell.csv'
    if mp.exists():
        for r in readcsv(mp):
            key = (norm(r.get('Name')), (r.get('Tag') or '').strip())
            if (r.get('Wert') or '').strip() == '0':
                tags.pop(key, None)
            elif key[0] and key[1]:
                tags[key] = ('manuell', (r.get('Beleg') or '').strip())
    info = {norm(z['Name']): z for z in zeilen}
    with (DATEN / 'karten_tags.csv').open('w', encoding='utf-8-sig', newline='') as f:
        w = csv.writer(f, delimiter=';')
        w.writerow(['Name', 'Typ', 'Domaene', 'Kosten', 'Spielbar', 'Tag', 'Quelle', 'Beleg'])
        for (n, tag), (quelle, beleg) in sorted(tags.items()):
            z = info.get(n)
            if z:
                w.writerow([z['Name'], z['Typ'], z['Domaene'], z['Kosten'], z['Spielbar'], tag, quelle, beleg])
    print(f'Karten: {len(zeilen)} | offene Zuordnungen: {len(offen)} | Tags: {len(tags)}')


if __name__ == '__main__':
    main()
