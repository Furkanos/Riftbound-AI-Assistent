# Projektstand: Aktualisierung `wissen/08_archetypen.md`

**Dokumentationsstand:** 25.11.2026. **Status:** Recherche-/Entscheidungsschritte noch nicht abgeschlossen; `wissen/08_archetypen.md` wurde im Rahmen dieses Arbeitsauftrags nicht aktualisiert.

> **Evidenzhinweis:** Die folgenden Arbeitszahlen und Einzelresultate sind im vorliegenden delegierten Chatkontext genannt, aber nicht unabhängig durch die angeforderten Recherche-PSVs im Repo belegbar. Die spezifischen lokalen Dateien `schritt2a_*`, `schritt2b_*_20261124*`, `paketsummen_8spalten_20261124.psv` und `*_rundeA/B_*` waren im lokalen Arbeitsbereich `/mnt/user-data/outputs` nicht vorhanden. Sie liegen daher nicht als verifizierbare Belege vor. Kennzeichnung „laut Chatverlauf, nicht im Repo belegt“ bleibt erforderlich.

## Zweck der Aktualisierung

`wissen/08_archetypen.md` ist im Repo ein Archiv-/Auswertungsstand vom 17.11.2026. Im lokalen Dateikopf steht: 24 Legenden, 25 Legendeneinträge (Diana doppelt gedruckt), 78 unabhängig verifizierte Turnierlisten, Platz ≤64 und maximal fünf Listen je Legende. Die laufende Aufgabe soll prüfen, ob neuere Listen und vorhandene Kandidaten korrekt berücksichtigt werden, bevor eine neue 08-Fassung entworfen wird. Der Repo-Stand wurde hier nicht geändert.

## Methode und Auswahlfilter

**Laut Chatverlauf, nicht im Repo belegt:**

1. Quellen für Einzelbelege: `riftbound.org`, `riftwatch.gg`, `riftbench.com`.
2. Kandidaten nach Eventdatum ab 24.10.2026 (einschließlich) auswählen.
3. Nur Platzierungen 1 bis 64 einschließlich als gültig zählen.
4. Testevents ausschließen.
5. Bannnamen der verwendeten Karten gegen Bannliste prüfen.
6. Kartennamen und Drucke/Setnummern gegen den Kartenpool abgleichen.
7. Fehlendes Datum, Platz, unvollständige Belegliste oder Druckunsicherheit als `[BITTE PRÜFEN]` behandeln, nicht stillschweigend entscheiden.
8. „Keine Turnierlisten gefunden“ bedeutet nur, dass in der beschriebenen Recherche keine Liste gefunden wurde, nicht dass es keine gibt.

Das konkrete Skript, die Suchabfragen, vollständige Linklisten, Einzelkarten-Decklisten und die Summenberechnung sind im Repo nicht dokumentiert. Sie müssen anhand der lokalen Recherchebelege rekonstruiert/geprüft werden, bevor die Zahlen als auditierbare Ergebnisse gelten.

## Arbeitszahlen je Block

### Block 1 – neue RAD-Legenden

**Laut Chatverlauf, nicht im Repo belegt:** Neun RAD-Legenden wurden bearbeitet; Chatstatus nennt **41 gültige Listen** und **5 `[BITTE PRÜFEN]`-Fälle**. Diese Summen werden hier nicht eigenständig aus Listen nachgerechnet. Die ermittelten Legendenbezeichnungen und Einzelbelege liegen nicht in der Repo-Version von 08 als neue, nachvollziehbare Blocktabelle vor. Vollständige Aufteilung je Legende, Quellenlinks und Zuordnung der fünf Prüffälle: **[BITTE PRÜFEN]**.

### Block 2a – Kandidaten aus den bereits in 08 verzeichneten 78 Links

**Laut Chatverlauf, nicht im Repo belegt:** 21 Kandidaten überprüft, davon **15 gültig** und **6 Nexus-Night-Kandidaten** mit unklarem Datum 23./24.10.2026. Diese sechs Fälle können mit dem Stichtagsfilter unterschiedlich eingeordnet werden; ohne belastbares Eventdatum sind sie offen. Die 21 konkreten Links und Einzelergebnisse sind in der hier verfügbaren Repo-Dokumentation nicht vorhanden. Dateibelege `schritt2a_*` fehlten lokal: `[BITTE PRÜFEN]`.

### Block 2b – Suche nach Listen für Poppy, Renata Glasc und Sivir

**Laut Chatverlauf, nicht im Repo belegt:**

| Legende/Champion | Kandidat | Chatstatus | Caveat |
|---|---|---|---|
| Poppy | `UNL/203` | keine Turnierlisten gefunden | zusätzlicher Vermerk zu Riftwatch-Druck `UNL-237/219`; exakter Druck und Quelle prüfen |
| Renata Glasc | `SFD/201` | keine Turnierlisten gefunden | Druck/Nummer separat vom Championnamen prüfen |
| Sivir | `SFD/203` | keine Turnierlisten gefunden | Druck/Nummer separat vom Championnamen prüfen |

„Keine gefunden“ darf nicht als Nichtexistenz ausgegeben werden. Suchraum, geprüfte Seiten und Abrufdatum: `[BITTE PRÜFEN]`; `schritt2b_*_20261124*` war nicht vorhanden.

## Offene Entscheidungen – Schritt 3

1. Die fünf RAD-Fälle `[BITTE PRÜFEN]` einzeln anhand ihrer Primärquellen klären oder ausdrücklich als ungeklärt stehen lassen.
2. Die sechs Nexus-Night-Belege mit unklarem 23./24.10.-Datum einzeln entscheiden: Datum aus belastbarer Eventquelle belegen, sonst nicht in den nach Stichtag zählenden Pool aufnehmen und Unsicherheit ausweisen.
3. Druckvermerk Poppy: unterscheiden, ob `UNL/203` und erwähnter Riftwatch-Druck `UNL-237/219` dieselbe Karte, anderer Druck oder Fehler im Datensatz ist. Nicht zusammenführen ohne Kataloggegenprobe.
4. Für sämtliche Kandidaten Set/Nummer-Schreibweisen normalisieren, dabei Rohbeleg erhalten. Beispiele `201`/`221` dürfen nicht durch Namensähnlichkeit vertauscht werden.
5. Doppeldrucke, insbesondere Diana (`UNL/197`, `UNL/234` laut Kontext), getrennt nachvollziehbar halten.
6. Summen aus Quellenprotokoll reproduzierbar neu berechnen; für jeden Beleg Event, Datum, Platz, Legende/Champion, Druck, Testeventstatus, Bannlistenabgleich, Poolabgleich und URL nachhalten.

## Schritt 4 – noch nicht ausgeführt

`wissen/08_archetypen.md` neu entwerfen und schreiben ist offen und wurde nicht ausgeführt. Im Arbeitskontext ausdrücklich: erst nach abgeschlossenem Schritt 3 und nur auf konkreten Auftrag. Vor dem Schreiben müssen die 41/15 etc. Summen mit den lokalen PSV-Belegen programmatisch kontrolliert und alle offenen Prüffälle dokumentiert sein.

## Fehlende Belege und lokale Dateien

Erwartete Recherchedateien zur Verifikation, angefragt für diesen Auftrag:

- `schritt2a_*`
- `schritt2b_*_20261124*`
- `paketsummen_8spalten_20261124.psv`
- `*_rundeA_*` und `*_rundeB_*`

Sie waren bei der Inventur von `/mnt/user-data/outputs` und `/mnt/user-data/uploads` nicht vorhanden. Es wurden stattdessen lokale ältere Audit-/Statusdateien vorgefunden, darunter `rad_step1_status.md`, `rad_link_audit.py` und `audit_riftbound_projekt.md`; diese belegen nicht die oben genannten Schritt-2-Zahlen. Keine davon wurde ins Repo kopiert.

## Abschlusskriterien für die nächste Bearbeitung

- Alle erwarteten Belegdateien bereitstellen oder Recherche erneut aus Primärquellen ausführen.
- Pro Liste Datum und Rang auf der Quelle prüfen; URL-Nummer nicht als Platzierungsbeleg interpretieren.
- Filter maschinell anwenden, Ausschlüsse/Unklarheiten sichtbar ausweisen und Summen doppelt reproduzieren.
- Format-/Bannliste mit dem zum Event passenden Stand prüfen und Kartenpoolabgleich dokumentieren.
- Schritt 3 Entscheidungen festhalten; erst danach für Schritt 4 gesonderten Auftrag einholen.
