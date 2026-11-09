#!/usr/bin/env python3
"""Besitz- und Legalitätscheck für Riftbound-Decks; nur Python-Standardbibliothek."""
import csv, re, unicodedata
from collections import defaultdict
from decimal import Decimal
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
AREAS={'Legende','Champion','Main','Battlefield','Rune','Sideboard'}
LEGAL={'OGS','OGN','SFD','UNL','VEN','RAD'}

def norm(s):
 s=unicodedata.normalize('NFKD',str(s or '')).encode('ascii','ignore').decode().casefold()
 s=re.sub(r'\[(?:foil|alternate\s*art|alt\s*art)[^]]*\]',' ',s)
 s=re.sub(r'\([^)]*(?:alternate art|overnumbered|signature|metal)[^)]*\)',' ',s)
 s=re.sub(r'\s+#\s*[a-z]*\d+[a-z]*\s*$',' ',s,flags=re.I)
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
def main():
 invs=sorted((ROOT/'wissen').glob('*Karten (Karten)*.csv'))
 cats=sorted((ROOT/'wissen').glob('*Kartenkatalog*.csv'))
 if not invs or not cats: raise SystemExit('Inventar oder Kartenkatalog fehlt in wissen/.')
 invkey=defaultdict(lambda:[0,[]]); invname=defaultdict(lambda:[0,[]])
 for r in readcsv(invs[0]):
  nm=r.get('Titel',''); k=(r.get('SetCode','').strip().upper(),num(r.get('Kartennummer'))); q=int(dec(r.get('Owned'))); price=dec(r.get('PriceEUR'))
  for d,key in ((invkey,k),(invname,norm(nm))):
   d[key][0]+=q
   if price>0: d[key][1].append((price,max(q,1)))
 ckey=defaultdict(list); cname=defaultdict(list)
 for r in readcsv(cats[0]):
  nm=r.get('Name') or r.get('Spielkartenname') or ''; k=(r.get('SetCode','').strip().upper(),num(r.get('Kartennummer')))
  if nm: ckey[k].append(nm); cname[norm(nm)].append((k[0],nm))
 fmt=ROOT/'wissen/02_format.md'; bans=set(); table=False
 for line in fmt.read_text(encoding='utf-8').splitlines():
  if 'Bannliste Standard' in line: table=True; continue
  if table and line.startswith('## '): break
  if table and line.startswith('|') and not re.match(r'\|\s*[-: ]+\|',line):
   a=[x.strip() for x in line.strip('|').split('|')]
   if a and a[0].casefold()!='karte': bans.add(norm(a[0]))
 outdir=ROOT/'ergebnis'; outdir.mkdir(exist_ok=True)
 for p in sorted((ROOT/'decks').glob('*.csv')):
  if p.name.upper()=='VORLAGE.CSV': continue
  lines=p.read_text(encoding='utf-8-sig').splitlines(); comments=[x[1:].strip() for x in lines if x.lstrip().startswith('#')]
  body='\n'.join(x for x in lines if not x.lstrip().startswith('#')); rows=list(csv.DictReader(body.splitlines(),delimiter=';'))
  cards=[]
  for i,r in enumerate(rows,2):
   if not r or not any(r.values()): continue
   q=int(r['Anzahl']); a=r['Bereich'].strip(); nm=r['Name'].strip()
   if q<1 or a not in AREAS or not nm: raise ValueError(f'{p}:{i}: ungültige Anzahl, Name oder Bereich')
   cards.append((q,nm,r.get('Set','').strip().upper(),r.get('Nummer','').strip(),a))
  results=[]; issues=[]; need=owned=missing=0; cost=Decimal(0); costok=True; counts=defaultdict(int); areas=defaultdict(int); legalcards=True
  for q,nm,st,no,area in cards:
   n=norm(nm); k=(st,num(no)); catalog=bool(ckey.get(k) or cname.get(n));
   if not catalog: issues.append(f'Katalog: **{nm}** nicht gefunden.'); legalcards=False
   if n in bans: issues.append(f'Gebannt: **{nm}** steht auf der Bannliste.'); legalcards=False
   if st not in LEGAL and not any(s in LEGAL for s,_ in cname.get(n,[])): legalcards=False
   stock=invkey.get(k) if st and no else None
   if not stock: stock=invname.get(n)
   have=stock[0] if stock else 0; miss=max(0,q-have); prices=stock[1] if stock else []
   price=sum((v*w for v,w in prices),Decimal(0))/sum(w for _,w in prices) if prices else None
   c=price*miss if price is not None else None
   if miss and c is None: costok=False
   if c is not None: cost+=c
   results.append((q,nm,st,no,min(q,have),miss,price,c)); need+=q; owned+=min(q,have); missing+=miss; areas[area]+=q
   if area in ('Main','Champion','Sideboard'): counts[n]+=q
  with (outdir/f'{p.stem}_deckcheck.csv').open('w',encoding='utf-8-sig',newline='') as f:
   w=csv.writer(f,delimiter=';'); w.writerow(['Karte','Set','Nummer','Benötigt','Besitz','Fehlend','Preis_€','Kosten_Fehlend_€'])
   for q,nm,st,no,h,m,pr,c in results: w.writerow([nm,st,no,q,h,m,f'{pr:.2f}' if pr is not None else '',f'{c:.2f}' if c is not None else ''])
   w.writerow(['SUMME','','',need,owned,missing,'',f'{cost:.2f}' if costok else ''])
  maincount=areas['Main']+areas['Champion']; bfs=[norm(n) for q,n,s,no,a in cards if a=='Battlefield']
  tests=[('Main Deck = 40 (Champion einschließlich)',maincount==40,f'{maincount}/40'),('Genau 1 Legende',areas['Legende']==1,f'{areas["Legende"]} eingetragen'),('Genau 12 Runen',areas['Rune']==12,f'{areas["Rune"]}/12'),('Genau 3 Battlefields',areas['Battlefield']==3,f'{areas["Battlefield"]}/3'),('Battlefields unterschiedlich',len(bfs)==len(set(bfs)),'Namen verschieden' if len(bfs)==len(set(bfs)) else 'Doppelte Namen'),('Max. 3 Exemplare je Name (Main + Sideboard)',max(counts.values(),default=0)<=3,'keine Überschreitung' if max(counts.values(),default=0)<=3 else 'Überschreitung'),('Alle Karten im Katalog',legalcards,'Katalog-/Format-/Bannlistenabgleich'),('Keine gebannte Karte',not any(norm(n) in bans for q,n,s,no,a in cards),'Bannliste aus wissen/02_format.md'),('Sideboard höchstens 10',areas['Sideboard']<=10,f'{areas["Sideboard"]}/10')]
  with (outdir/f'{p.stem}_legalitaet.md').open('w',encoding='utf-8') as f:
   incomplete=any('UNVOLLSTÄNDIG' in x.upper() for x in comments)
   f.write(f'# Legalitätscheck: {p.stem}\n\n**Deckliste: {"UNVOLLSTÄNDIG" if incomplete else "nicht als unvollständig markiert"}.**\n\n| Prüfung | Ergebnis | Details |\n|---|---|---|\n')
   for label,ok,detail in tests: f.write(f'| {label} | {"BESTANDEN" if ok else "NICHT BESTANDEN"} | {detail} |\n')
   f.write('\n## Zuordnung und Besitz\n\nBesitzabgleich zuerst nach Set+Nummer (Foil/Normal werden addiert), sonst normalisiertem Namen. CSV wird mit Python-CSV-Parser gelesen.\n\n')
   if issues: f.write('Hinweise:\n'+''.join(f'- {x}\n' for x in issues))
   else: f.write('Keine fehlenden Katalogzuordnungen oder Bannlistentreffer.\n')
   if not costok: f.write('\nPreise für fehlende Exemplare sind nicht im Inventar enthalten; Kostenfelder bleiben deshalb leer, nicht €0.\n')
   if incomplete: f.write('\nDie Liste enthält nur bestätigte Karten; vollständige Decklegalität kann damit nicht bewertet werden.\n')
   f.write(f'\nBenötigt **{need}** · Besitz **{owned}** · Fehlend **{missing}** · Kosten **{f"€{cost:.2f}" if costok else "nicht vollständig bestimmbar"}**.\n')
if __name__=='__main__': main()
