#!/usr/bin/env python3
"""Riftbound deck ownership and Standard legality check; standard library only."""
import csv, json, re, unicodedata
from collections import defaultdict
from decimal import Decimal
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
AREAS={'Legende','Champion','Main','Battlefield','Rune','Sideboard'}
AREA_ALIASES={'Runen':'Rune','Battlefields':'Battlefield'}
LEGAL={'OGS','OGN','SFD','UNL','VEN','RAD'}

def norm(s):
 s=unicodedata.normalize('NFKD',str(s or '')).encode('ascii','ignore').decode().casefold()
 s=re.sub(r'\[(?:foil|alternate\s*art|alt\s*art)[^]]*\]',' ',s)
 s=re.sub(r'\([^)]*(?:alternate art|overnumbered|signature|metal)[^)]*\)',' ',s)
 s=re.sub(r'\s*#\s*[a-z]*\d+[a-z]*\s*$',' ',s,flags=re.I)
 return ' '.join(re.sub(r'[^a-z0-9]+',' ',s).split())
def num(s): return re.sub(r'[a-z]+$','',str(s or '').strip().casefold())
def readcsv(p,delims=',;\t|'):
 with p.open(encoding='utf-8-sig',newline='') as f:
  sample=f.read(8192); f.seek(0)
  try: d=csv.Sniffer().sniff(sample,delimiters=delims)
  except csv.Error: d=csv.excel
  return list(csv.DictReader(f,dialect=d))
def dec(x):
 try: return Decimal(str(x or '0').replace(',','.'))
 except Exception: return Decimal(0)
def arr(s):
 try: return json.loads(s) if str(s or '').strip().startswith('[') else []
 except Exception: return []
def main():
 invs=sorted((ROOT/'wissen').glob('*Karten (Karten)*.csv')); cats=sorted((ROOT/'wissen').glob('*Kartenkatalog*.csv'))
 if not invs or not cats: raise SystemExit('Inventar oder Kartenkatalog fehlt in wissen/.')
 # Aggregate owned copies and market price by exact set+number and normalized title.
 invkey=defaultdict(lambda:{'owned':0,'prices':[]}); invname=defaultdict(lambda:{'owned':0,'prices':[]})
 for r in readcsv(invs[0]):
  nm=r.get('Titel',''); k=(r.get('SetCode','').strip().upper(),num(r.get('Kartennummer'))); q=int(dec(r.get('Owned'))); price=dec(r.get('PriceEUR'))
  for d,key in ((invkey,k),(invname,norm(nm))):
   d[key]['owned']+=q
   if price>0: d[key]['prices'].append((price,max(q,1)))
 ckey=defaultdict(list); cname=defaultdict(list)
 for r in readcsv(cats[0]):
  nm=r.get('Name') or r.get('Spielkartenname') or ''; k=(r.get('SetCode','').strip().upper(),num(r.get('Kartennummer')))
  if nm: ckey[k].append(r); cname[norm(nm)].append(r)
 fmt=(ROOT/'wissen/02_format.md').read_text(encoding='utf-8'); bans=set(); table=False
 for line in fmt.splitlines():
  if 'Bannliste Standard' in line: table=True; continue
  if table and line.startswith('## '): break
  if table and line.startswith('- '): bans.add(norm(line[2:].strip()))
 outdir=ROOT/'ergebnis'; outdir.mkdir(exist_ok=True)
 for p in sorted((ROOT/'decks').glob('*.csv')):
  if p.name.upper()=='VORLAGE.CSV': continue
  lines=p.read_text(encoding='utf-8-sig').splitlines(); comments=[x[1:].strip() for x in lines if x.lstrip().startswith('#')]
  rows=list(csv.DictReader([x for x in lines if not x.lstrip().startswith('#')],delimiter=';'))
  cards=[]
  for i,r in enumerate(rows,2):
   if not r or not any(r.values()): continue
   q=int(r['Anzahl']); a=r['Bereich'].strip(); a=AREA_ALIASES.get(a,a); nm=r['Name'].strip(); st=r.get('Set','').strip().upper(); no=r.get('Nummer','').strip()
   if q<1 or a not in AREAS or not nm: raise ValueError(f'{p}:{i}: ungültige Anzahl, Name oder Bereich')
   cards.append({'q':q,'name':nm,'set':st,'no':no,'area':a,'key':(st,num(no)),'cat':None})
  # Choose the catalog printing matching requested set+number; otherwise name lookup for diagnosis only.
  issues=[]; all_catalog=True
  for c in cards:
   matches=ckey.get(c['key'],[])
   chosen=next((r for r in matches if norm(r.get('Name') or r.get('Spielkartenname'))==norm(c['name'])),None)
   if chosen is None:
    all_catalog=False
    if matches or cname.get(norm(c['name'])): issues.append(f"Katalogabweichung: **{c['name']}** – {c['set']} {c['no']} stimmt nicht mit dem Namens-/Seteintrag überein.")
    else: issues.append(f"Katalog: **{c['name']}** nicht gefunden.")
   c['cat']=chosen
   if norm(c['name']) in bans: issues.append(f"Gebannt: **{c['name']}** steht auf der Bannliste.")
  # Ownership is allocated once per physical copy across duplicate deck rows.
  remaining_key={k:v['owned'] for k,v in invkey.items()}; remaining_name={k:v['owned'] for k,v in invname.items()}
  results=[]; need=owned=missing=0; costs=Decimal(0); costok=True; counts=defaultdict(int); areas=defaultdict(int)
  for c in cards:
   n=norm(c['name']); q=c['q']; k=c['key']; stock=invkey.get(k) if c['set'] and c['no'] else None; matched='Set+Nummer'
   if not stock or stock['owned']==0:
    stock=invname.get(n); matched='Name (Fallback)'
   stock=stock or {'owned':0,'prices':[]}
   # Rune cards are always available, regardless of inventory quantities.
   is_rune=c['area']=='Rune' or (c['cat'] and str(c['cat'].get('Typ') or '').strip().casefold()=='rune')
   if is_rune:
    have=q; miss=0; price=Decimal(0); cost=Decimal(0)
   else:
    # Consume by exact key when available; fallback pool is separately de-duplicated.
    name_avail=remaining_name.get(n,0)
    avail=min(remaining_key.get(k,0),name_avail) if matched=='Set+Nummer' else name_avail
    have=min(q,avail)
    remaining_name[n]=name_avail-have
    if matched=='Set+Nummer': remaining_key[k]=remaining_key.get(k,0)-have
    miss=q-have; prices=stock['prices']; price=sum((v*w for v,w in prices),Decimal(0))/sum(w for _,w in prices) if prices else None
    cost=price*miss if price is not None else None
   if miss and cost is None: costok=False
   if cost is not None: costs+=cost
   results.append((q,c['name'],c['area'],c['set'],c['no'],have,miss,price,cost,matched))
   need+=q; owned+=have; missing+=miss; areas[c['area']]+=q
   if c['area'] in ('Main','Champion','Sideboard'): counts[n]+=q
  with (outdir/f'{p.stem}_deckcheck.csv').open('w',encoding='utf-8-sig',newline='') as f:
   w=csv.writer(f,delimiter=';'); w.writerow(['Bereich','Karte','Set','Nummer','Benötigt','Besitz','Fehlend','Preis_€','Kosten_Fehlend_€'])
   for q,nm,area,st,no,h,m,pr,cost,matched in results: w.writerow([area,nm,st,no,q,h,m,f'{pr:.2f}' if pr is not None else '',f'{cost:.2f}' if cost is not None else ''])
   w.writerow(['SUMME','','','',need,owned,missing,'',f'{costs:.2f}' if costok else ''])
  with (outdir/f'{p.stem}_kaufliste.csv').open('w',encoding='utf-8-sig',newline='') as f:
   w=csv.writer(f,delimiter=';'); w.writerow(['Bereich','Anzahl','Name','Set','Nummer','Besitz','Fehlend','Preis_€','Kosten_€','Hinweis'])
   for q,nm,area,st,no,h,m,pr,cost,matched in results:
    if m: w.writerow([area,q,nm,st,no,h,m,f'{pr:.2f}' if pr is not None else '',f'{cost:.2f}' if cost is not None else '', '' if pr is not None else 'PREIS FEHLT'])
  maincount=areas['Main']+areas['Champion']; bfs=[norm(c['name']) for c in cards if c['area']=='Battlefield']
  domains=[]; signatures=[]; legend_tags=[]; champion_tags=[]
  for c in cards:
   r=c['cat']
   if r:
    domains.extend((c,d) for d in arr(r.get('Domaenen')) if str(d).casefold()!='colorless')
    if 'signature' in str(r.get('Supertyp') or '').casefold(): signatures.append(c)
    if c['area']=='Legende': legend_tags=arr(r.get('Tags'))
    if c['area']=='Champion': champion_tags=arr(r.get('Tags'))
  identity={str(d).casefold() for c,d in domains if c['area']=='Legende'}
  domain_bad=[f"{c['name']} ({d})" for c,d in domains if c['area'] not in ('Legende','Rune') and str(d).casefold() not in identity]
  rune_bad=[f"{c['name']} ({d})" for c,d in domains if c['area']=='Rune' and str(d).casefold() not in identity]
  tests=[('Main Deck = 40 (Champion einschließlich)',maincount==40,f'{maincount}/40'),('Genau 1 Legende',areas['Legende']==1,f'{areas["Legende"]} eingetragen'),('Genau 12 Runen',areas['Rune']==12,f'{areas["Rune"]}/12'),('Genau 3 Battlefields',areas['Battlefield']==3,f'{areas["Battlefield"]}/3'),('Battlefields unterschiedlich',len(bfs)==len(set(bfs)),'Namen verschieden' if len(bfs)==len(set(bfs)) else 'Doppelte Namen'),('Max. 3 Exemplare je Name (Main + Sideboard)',max(counts.values(),default=0)<=3,'keine Überschreitung' if max(counts.values(),default=0)<=3 else 'Überschreitung'),('Alle Karten Set/Nummer im Katalog',all_catalog,'Katalogabgleich'),('Keine gebannte Karte',not any(norm(c['name']) in bans for c in cards),'Bannliste aus wissen/02_format.md'),('Sideboard höchstens 10',areas['Sideboard']<=10,f'{areas["Sideboard"]}/10'),('Alle Domains entsprechen Legendenidentität',not domain_bad,', '.join(domain_bad) if domain_bad else 'keine Fremd-Domains; Identität '+', '.join(sorted(identity))),('Runen-Domains entsprechen Legendenidentität',not rune_bad,', '.join(rune_bad) if rune_bad else 'Runen passen zu '+', '.join(sorted(identity))),('Chosen Champion Tag passt zur Legende',bool(set(legend_tags)&set(champion_tags)),f'Legend: {legend_tags}; Champion: {champion_tags}'),('Höchstens 3 Signatures',len(signatures)<=3,f'{len(signatures)}/3')]
  with (outdir/f'{p.stem}_legalitaet.md').open('w',encoding='utf-8') as f:
   incomplete=any('UNVOLLSTÄNDIG' in x.upper() for x in comments)
   f.write(f'# Legalitätscheck: {p.stem}\n\n| Bereich | Anzahl |\n|---|---:|\n')
   for a in ('Legende','Champion','Main','Rune','Battlefield','Sideboard'): f.write(f'| {a} | {areas[a]} |\n')
   f.write(f'\n**Deckliste: {"UNVOLLSTÄNDIG" if incomplete else "vollständig markiert"}.**\n\n| Prüfung | Ergebnis | Details |\n|---|---|---|\n')
   for label,ok,detail in tests: f.write(f'| {label} | {"BESTANDEN" if ok else "NICHT BESTANDEN"} | {detail} |\n')
   f.write('\n## Zuordnung und Besitz\n\nBesitzabgleich nach Set+Nummer; Foil-/Normal- und Showcase-Bestand wird über Set+Nummer summiert. Fallback: normalisierter Name (einschließlich Entfernen von `[Foil]` und `#Nummer`). Bestand wird bei mehrfachen Decklistenzeilen nur einmal angerechnet. Runen gelten als unbegrenzt vorhanden; sie werden vollständig als Besitz ausgewiesen und verursachen keine Fehlmenge oder Kosten.\n\n')
   f.write(('Hinweise:\n'+''.join(f'- {x}\n' for x in issues)) if issues else 'Keine fehlenden Katalogzuordnungen oder Bannlistentreffer.\n')
   if not costok: f.write('\nPreise für fehlende Exemplare sind im Inventar nicht verfügbar; entsprechende Kosten bleiben leer.\n')
   if incomplete: f.write('\nDie Liste ist als unvollständig markiert.\n')
   f.write(f'\nBenötigt **{need}** · Besitz **{owned}** · Fehlend **{missing}** · Kosten **{f"€{costs:.2f}" if costok else "nicht vollständig bestimmbar"}**.\n')
if __name__=='__main__': main()
