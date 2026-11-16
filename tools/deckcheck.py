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
AREA_ORDER=('Legende','Champion','Main','Sideboard','Battlefield','Rune')

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
def pick(r,*names,anytext=False):
 for n in names:
  v=r.get(n)
  if v not in (None,''): return ' '.join(str(v).split())
 if anytext:
  for k,v in r.items():
   if k and 'text' in k.casefold() and v: return ' '.join(str(v).split())
 return ''

def main():
 invs=sorted((ROOT/'wissen').glob('*Karten (Karten)*.csv')); cats=sorted((ROOT/'wissen').glob('*Kartenkatalog*.csv'))
 if not invs or not cats: raise SystemExit('Inventar oder Kartenkatalog fehlt in wissen/.')
 # Aggregate owned copies and market price by exact set+number and normalized title.
 invkey=defaultdict(lambda:{'owned':0,'prices':[]}); invname=defaultdict(lambda:{'owned':0,'prices':[]}); invkey_names=defaultdict(lambda:defaultdict(int))
 for r in readcsv(invs[0]):
  nm=r.get('Titel',''); k=(r.get('SetCode','').strip().upper(),num(r.get('Kartennummer'))); q=int(dec(r.get('Owned'))); price=dec(r.get('PriceEUR'))
  for d,key in ((invkey,k),(invname,norm(nm))):
   d[key]['owned']+=q
   if price>0: d[key]['prices'].append((price,max(q,1)))
  invkey_names[k][norm(nm)]+=q
 ckey=defaultdict(list); cname=defaultdict(list)
 for r in readcsv(cats[0]):
  nm=r.get('Name') or r.get('Spielkartenname') or ''; k=(r.get('SetCode','').strip().upper(),num(r.get('Kartennummer')))
  if nm: ckey[k].append(r); cname[norm(nm)].append(r)
 # Card texts from 03_kartenpool.csv (primary source), catalog as fallback.
 pkey={}; pname={}
 pool=ROOT/'wissen/03_kartenpool.csv'
 if pool.exists():
  for r in readcsv(pool):
   k=(str(r.get('Set') or '').strip().upper(),num(r.get('Nummer')))
   pkey.setdefault(k,r); pname.setdefault(norm(r.get('Name')),r)
 def info(k,nm,cat):
  p=pkey.get(k); mismatch=bool(p and norm(p.get('Name'))!=norm(nm))
  if mismatch: p=None
  p=p or pname.get(norm(nm)) or {}; cat=cat or {}
  text=pick(p,'Kartentext','Text',anytext=True) or pick(cat,'Kartentext','Text','Regeltext','Effekt','Effekttext','Beschreibung',anytext=True)
  if mismatch and not pname.get(norm(nm)): text='[WARNUNG: Name und Set-Nummer passen nicht zusammen]'
  typ=pick(p,'Typ') or pick(cat,'Typ','Kartentyp')
  dom=pick(p,'Domäne','Domaene','Domänen') or ', '.join(str(d) for d in arr(cat.get('Domaenen')))
  cost=pick(p,'Kosten') or pick(cat,'Kosten','Energie')
  stats=pick(p,'Stats') or pick(cat,'Might','Stats')
  return typ,dom,cost,stats,text
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
  remaining_key_names={k:dict(v) for k,v in invkey_names.items()}
  def consume_key(key,quantity):
   """Allocate copies from one printing and synchronize its inventory-title aliases."""
   taken=min(quantity,remaining_key.get(key,0)); remaining_key[key]=remaining_key.get(key,0)-taken
   left=taken
   for alias in sorted(remaining_key_names.get(key,{})):
    amount=min(left,remaining_key_names[key][alias]); remaining_key_names[key][alias]-=amount
    remaining_name[alias]=max(remaining_name.get(alias,0)-amount,0); left-=amount
    if left==0: break
   return taken
  def consume_name(name,quantity):
   """Allocate by inventory name and release matching keyed copies, when known."""
   taken=min(quantity,remaining_name.get(name,0)); remaining_name[name]=remaining_name.get(name,0)-taken
   left=taken
   for key in sorted(remaining_key_names):
    amount=min(left,remaining_key_names[key].get(name,0))
    if amount:
     remaining_key_names[key][name]-=amount; remaining_key[key]=max(remaining_key.get(key,0)-amount,0); left-=amount
    if left==0: break
   return taken
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
    # A validated exact catalog key wins; name-only rows consume that same keyed pool.
    if matched=='Set+Nummer' and c['cat']:
     have=consume_key(k,q)
    elif cname.get(n):
     candidate_keys=sorted({(str(row.get('SetCode') or '').strip().upper(),num(row.get('Kartennummer'))) for row in cname.get(n,[])})
     have=0
     for candidate_key in candidate_keys:
      used=consume_key(candidate_key,q-have); have+=used
      if have==q: break
    else:
     have=consume_name(n,q)
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
   missing_rows=[r for r in results if r[6]]
   if not missing_rows: w.writerow(['KEINE FEHLENDEN KARTEN'])
   for q,nm,area,st,no,h,m,pr,cost,matched in missing_rows:
    w.writerow([area,q,nm,st,no,h,m,f'{pr:.2f}' if pr is not None else '',f'{cost:.2f}' if cost is not None else '', '' if pr is not None else 'PREIS FEHLT'])
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
  tests=[('Main Deck = 40 (Champion einschließlich)',maincount==40,f'{maincount}/40'),('Genau 1 Legende',areas['Legende']==1,f'{areas[\"Legende\"]} eingetragen'),('Genau 12 Runen',areas['Rune']==12,f'{areas[\"Rune\"]}/12'),('Genau 3 Battlefields',areas['Battlefield']==3,f'{areas[\"Battlefield\"]}/3'),('Battlefields unterschiedlich',len(bfs)==len(set(bfs)),'Namen verschieden' if len(bfs)==len(set(bfs)) else 'Doppelte Namen'),('Max. 3 Exemplare je Name (Main + Sideboard)',max(counts.values(),default=0)<=3,'keine Überschreitung' if max(counts.values(),default=0)<=3 else 'Überschreitung'),('Alle Karten Set/Nummer im Katalog',all_catalog,'Katalogabgleich'),('Keine gebannte Karte',not any(norm(c['name']) in bans for c in cards),'Bannliste aus wissen/02_format.md'),('Sideboard höchstens 10',areas['Sideboard']<=10,f'{areas[\"Sideboard\"]}/10'),('Alle Domains entsprechen Legendenidentität',not domain_bad,', '.join(domain_bad) if domain_bad else 'keine Fremd-Domains; Identität '+', '.join(sorted(identity))),('Runen-Domains entsprechen Legendenidentität',not rune_bad,', '.join(rune_bad) if rune_bad else 'Runen passen zu '+', '.join(sorted(identity))),('Chosen Champion Tag passt zur Legende',bool(set(legend_tags)&set(champion_tags)),f'Legend: {legend_tags}; Champion: {champion_tags}'),('Höchstens 3 Signatures',len(signatures)<=3,f'{len(signatures)}/3')]
  # Signature legality is strictly tied to the legend's champion tag.
  legend_tagset={str(tag).casefold() for tag in legend_tags}
  illegal_signatures=[]
  for signature in signatures:
   card_tags={str(tag).casefold() for tag in arr((signature.get('cat') or {}).get('Tags'))}
   if not (legend_tagset & card_tags): illegal_signatures.append(signature)
  from datenbasis import signature_info
  owned_signatures=signature_info()
  present_signature_names={norm(c['name']) for c in signatures}
  signature_warnings=[]
  for tag in legend_tags:
   for record in owned_signatures.get(str(tag), []):
    if norm(record['name']) not in present_signature_names:
     signature_warnings.append(record)
  with (outdir/f'{p.stem}_legalitaet.md').open('w',encoding='utf-8') as f:
   incomplete=any('UNVOLLSTÄNDIG' in x.upper() for x in comments)
   f.write(f'# Legalitätscheck: {p.stem}\n\n| Bereich | Anzahl |\n|---|---:|\n')
   for a in ('Legende','Champion','Main','Rune','Battlefield','Sideboard'): f.write(f'| {a} | {areas[a]} |\n')
   f.write(f'\n**Deckliste: {\"UNVOLLSTÄNDIG\" if incomplete else \"vollständig markiert\"}.**\n\n| Prüfung | Ergebnis | Details |\n|---|---|---|\n')
   for label,ok,detail in tests: f.write(f'| {label} | {\"BESTANDEN\" if ok else \"NICHT BESTANDEN\"} | {detail} |\n')
   f.write('\\n## Signature-Check\\n\\n')
   if illegal_signatures:
    for c in illegal_signatures:
     f.write(f\"- ❌ **{c['name']}** passt nicht zum Champion-Tag der Legende ({', '.join(legend_tags)}).\\n\")
   else:
    f.write('Keine enthaltene Signature widerspricht dem Champion-Tag der Legende.\\n')
   if signature_warnings:
    for record in sorted(signature_warnings,key=lambda r:r['name'].casefold()):
     f.write(f\"- ⚠️ **{record['name']}** ({record['set']}/{record['number']}), Besitz {record['owned']} – nicht im Deck. Kartentext: {record['text'] or '[Kartentext fehlt]' }\\n\")
   else:
    f.write('Keine passende, besessene Signature fehlt im Deck.\\n')
   f.write('\\n## Zuordnung und Besitz\\n\\nBesitzabgleich nach Set+Nummer; Foil-/Normal- und Showcase-Bestand wird über Set+Nummer summiert. Fallback: normalisierter Name (einschließlich Entfernen von `[Foil]` und `#Nummer`). Bestand wird bei mehrfachen Decklistenzeilen nur einmal angerechnet. Runen gelten als unbegrenzt vorhanden; sie werden vollständig als Besitz ausgewiesen und verursachen keine Fehlmenge oder Kosten.\\n\\n')
   f.write(('Hinweise:\\n'+''.join(f'- {x}\\n' for x in issues)) if issues else 'Keine fehlenden Katalogzuordnungen oder Bannlistentreffer.\\n')
   if not costok: f.write('\\nPreise für fehlende Exemplare sind im Inventar nicht verfügbar; entsprechende Kosten bleiben leer.\\n')
   if incomplete: f.write('\\nDie Liste ist als unvollständig markiert.\\n')
   f.write(f'\\nBenötigt **{need}** · Besitz **{owned}** · Fehlend **{missing}** · Kosten **{f\"€{costs:.2f}\" if costok else \"nicht vollständig bestimmbar\"}**.\\n')
  # Zusatzdatei 1: vollständige Kartentexte aller Deckkarten.
  deckq=defaultdict(int)
  for c in cards: deckq[norm(c['name'])]+=c['q']
  with (outdir/f'{p.stem}_kartentexte.md').open('w',encoding='utf-8') as f:
   f.write(f'# Kartentexte: {p.stem}\n\nQuelle: wissen/03_kartenpool.csv (Fallback: Kartenkatalog). Automatisch erzeugt – nicht von Hand ändern.\n')
   for a in AREA_ORDER:
    sel=[c for c in cards if c['area']==a]
    if not sel: continue
    f.write(f'\n## {a} ({sum(c[\"q\"] for c in sel)})\n')
    for c in sel:
     is_rune=c['area']=='Rune' or c['name'].strip().casefold().endswith('rune')
     if is_rune:
      cat=c['cat'] or {}
      dom=pick(cat,'Domäne','Domaene','Domänen') or ', '.join(str(d) for d in arr(cat.get('Domaenen'))) or '?'
      f.write(f\"\\n### {c['q']}× {c['name']} ({c['set']}-{c['no']})\\nRune – Basisressource (Domäne: {dom}), kein Kartentext\\n\")
     else:
      typ,dom,cost,stats,text=info(c['key'],c['name'],c['cat'])
      f.write(f\"\\n### {c['q']}× {c['name']} ({c['set']}-{c['no']})\\n- Typ: {typ or '?'} · Domäne: {dom or '?'} · Kosten: {cost or '?'} · Stats: {stats or '-'}\\n- Text: {text or '[TEXT FEHLT IN DEN DATEN – nicht verwenden, bevor geprüft]'}\\n\")
  # Zusatzdatei 2: legale Alternativen aus der Sammlung, passend zur Legendenidentität.
  alts=[]; seen=set()
  for k,v in invkey.items():
   if v['owned']<=0 or k[0] not in LEGAL or not ckey.get(k): continue
   cat=ckey[k][0]; nm=cat.get('Name') or cat.get('Spielkartenname') or ''; n=norm(nm)
   if not nm or n in seen or n in bans: continue
   doms={str(d).casefold() for d in arr(cat.get('Domaenen'))}-{'colorless'}
   if not identity or not doms<=identity: continue
   typ,dom,cost,stats,text=info(k,nm,cat); t=typ.casefold()
   if 'legend' in t or 'rune' in t or 'token' in t: continue
   seen.add(n); own=invname[n]['owned'] or v['owned']; used=deckq.get(n,0)
   frei=max(own-used,0); maxadd=frei if 'battlefield' in t else max(min(frei,3-used),0)
   alts.append((typ or '?',nm,k,own,used,maxadd,dom,cost,stats,text))
  alts.sort(key=lambda x:(x[0].casefold(),x[1].casefold()))
  with (outdir/f'{p.stem}_alternativen.md').open('w',encoding='utf-8') as f:
   f.write(f'# Alternativen aus der Sammlung: {p.stem}\\n\\nAlle Karten aus der Sammlung, die legal sind (Set legal, nicht gebannt) und zur Domänenidentität **{\", \".join(sorted(identity)) or \"unbekannt\"}** passen. Ohne Legenden, Runen und Tokens. Automatisch erzeugt.\\n\\n- **Besitz** = Exemplare in der Sammlung (alle Drucke)\\n- **Im Deck** = bereits in diesem Deck (alle Bereiche)\\n- **Max. zusätzlich** = so viele dürfen noch dazu (Besitz und 3er-Limit berücksichtigt)\\n\\nAnzahl Karten: {len(alts)}\\n')
   cur=None
   for typ,nm,k,own,used,maxadd,dom,cost,stats,text in alts:
    if typ!=cur: cur=typ; f.write(f'\\n## {typ}\\n')
    f.write(f\"\\n### {nm} ({k[0]}-{k[1]})\\n- Besitz: {own} · Im Deck: {used} · Max. zusätzlich: {maxadd}\\n- Domäne: {dom or '?'} · Kosten: {cost or '?'} · Stats: {stats or '-'}\\n- Text: {text or '[TEXT FEHLT IN DEN DATEN]'}\\n\")
if __name__=='__main__': main()
