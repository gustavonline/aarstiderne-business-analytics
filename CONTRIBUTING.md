# Contributing

Tak fordi du bidrager 🙌

## Branches

- `main`: stabil
- `develop`: integration
- `feature/*`: nye ændringer
- `death`: eksperiment/sandkasse

## Flow

1. `git checkout develop && git pull`
2. `git checkout -b feature/<dit-navn>`
3. Lav ændringer
4. Kør validering:
   - `python scripts/validate_data_model.py`
5. Commit + push
6. Opret PR til `develop`

Når noget er testet og godkendt, merges `develop` til `main`.

## Vigtigt

- Commit ikke `.pbi`, cache eller lokale settings
- Hold PRs små og fokuserede
- Opdater docs ved model-/measure-ændringer
