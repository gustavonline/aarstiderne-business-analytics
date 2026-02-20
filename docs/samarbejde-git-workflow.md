# Samarbejde (asynkront) – Git workflow

## Branch-strategi

- `main` = stabil version (kan altid åbnes)
- `develop` = integration af nye features
- `feature/<navn>` = hver opgave/ændring
- `death` = valgfri sandkasse/eksperiment-branch (kan slettes igen)

> Praktisk: arbejd normalt i `feature/*` og merge til `develop`. Merge derefter `develop -> main` når noget er testet.

---

## Daglig arbejdsgang

### 1) Start fra develop

```bash
git checkout develop
git pull
```

### 2) Opret feature-branch

```bash
git checkout -b feature/min-opgave
```

### 3) Lav ændringer

- Power BI: report/layout/measures
- Docs/scripts
- Undgå lokale cache-filer

### 4) Commit og push

```bash
git add .
git commit -m "feat: kort beskrivelse"
git push -u origin feature/min-opgave
```

### 5) Pull request

- PR: `feature/min-opgave` -> `develop`
- Få review
- Merge

### 6) Release til main

- PR: `develop` -> `main`
- Merge når stabil

---

## Aftale i teamet (anbefalet)

- Små commits med tydelige beskeder
- Ingen direkte commits til `main`
- Opdater `docs/` når model/measure ændres
- Kør `python scripts/validate_data_model.py` før PR

---

## Invite samarbejdspartner

På GitHub repoet:

1. `Settings`
2. `Collaborators`
3. `Add people`
4. Vælg din kammerats GitHub-brugernavn
