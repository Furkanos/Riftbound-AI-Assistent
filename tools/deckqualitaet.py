#!/usr/bin/env python3
"""Schreibt ergebnis/<deck>_qualitaet.md: Engine-Dichte, Kurve, Rollen je Deck.
Zahlen kommen nur aus daten/karten_tags.csv und daten/sammlung_normalisiert.csv."""
import csv, re, sys
from collections import defaultdict
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from deckcheck import norm, readcsv, AREA_ALIASES

ROOT = Path(__file__).resolve().parents[1]
DATEN = ROOT / 'daten'
ROLLEN = ['removal', 'gear_antwort', 'konter', 'xp_quelle', 'nicht_aus_hand', 'equipment',
          'waehlt_eigene_einheit', 'temporary', 'mech', 'karten_ziehen']


def kosten(s):
    m = re.match(r'\s*(\d+)', str(s or ''))
    return int(m.group(1)) if m else None


def main():
    if not (DATEN / 'karten_tags.csv').exists():
        raise SystemExit('Erst tools/datenbasis.py ausfuehren.')
    tags = defaultdict(dict)
    for r in readcsv(DATEN / 'karten_tags.csv'):
        tags[norm(r['Name'])][r['Tag']] = r['Quelle']
    karte = {norm(r['Name']): r for r in readcsv(DATEN / 'sammlung_normalisiert.csv')}
    engine = []
    ep = DATEN / 'legenden_engine.csv'
    if ep.exists():
        engine = readcsv(ep)
    out = ROOT / 'ergebnis'
    out.mkdir(exist_ok=True)
    for p in sorted((ROOT / 'decks').glob('*.csv')):
        if p.name.upper() == 'VORLAGE.CSV':
            continue
        lines = [x for x in p.read_text(encoding='utf-8-sig').splitlines() if not x.lstrip().startswith('#')]
        try:
            rows = list(csv.DictReader(lines, delimiter=';'))
        except Exception:
            continue
        main_k, side_k, legende = [], [], ''
        for r in rows:
            if not r or not r.get('Anzahl'):
                continue
            a = AREA_ALIASES.get(r['Bereich'].strip(), r['Bereich'].strip())
            q, n = int(r['Anzahl']), norm(r['Name'])
            if a in ('Main', 'Champion'):
                main_k.append((q, n, r['Name'].strip()))
            elif a == 'Sideboard':
                side_k.append((q, n, r['Name'].strip()))
            elif a == 'Legende':
                legende = r['Name'].strip()
        eng = next((e for e in engine if e.get('Legende_Prefix') and legende.casefold().startswith(e['Legende_Prefix'].casefold())), None)
        etag = (eng or {}).get('Engine_Tag', '')
        kurve = defaultdict(int)
        einheiten_bis3 = 0
        fehlt = []
        for q, n, name in main_k:
            k = karte.get(n)
            if not k:
                fehlt.append(name)
                continue
            c = kosten(k['Kosten'])
            kurve['?' if c is None else (str(c) if c < 6 else '6+')] += q
            if 'unit' in k['Typ'].casefold() and c is not None and c <= 3:
                einheiten_bis3 += q

        def zaehle(liste, tag):
            ges = sum(q for q, n, _ in liste if tag in tags.get(n, {}))
            auto = sum(q for q, n, _ in liste if tags.get(n, {}).get(tag) == 'auto')
            return ges, auto
        with (out / f'{p.stem}_qualitaet.md').open('w', encoding='utf-8') as f:
            f.write(f'# Deckqualitaet: {p.stem}\n\nAutomatisch erzeugt aus daten/. Spalte "davon auto" = ungepruefte Entwurfs-Tags.\n\n')
            f.write(f'Legende: **{legende or "?"}** | Engine-Tag: **{etag or "[nicht hinterlegt in daten/legenden_engine.csv]"}**\n\n')
            if etag:
                g, a = zaehle(main_k, etag)
                f.write(f'**Engine-Ausloeser im Main: {g}/40 (davon auto: {a})**\n\n')
            f.write(f'Einheiten mit Kosten <= 3: **{einheiten_bis3}**\n\n## Kurve (Main inkl. Champion)\n\n| Kosten | Kopien |\n|---|---:|\n')
            for s in ['0', '1', '2', '3', '4', '5', '6+', '?']:
                if kurve.get(s):
                    f.write(f'| {s} | {kurve[s]} |\n')
            f.write('\n## Rollen\n\n| Rolle | Main | davon auto | Sideboard |\n|---|---:|---:|---:|\n')
            for t in ROLLEN:
                g, a = zaehle(main_k, t)
                s, _ = zaehle(side_k, t)
                f.write(f'| {t} | {g} | {a} | {s} |\n')
            if fehlt:
                f.write('\n## Nicht in der Sammlung gefunden\n\n' + ''.join(f'- {x}\n' for x in fehlt))


if __name__ == '__main__':
    main()
