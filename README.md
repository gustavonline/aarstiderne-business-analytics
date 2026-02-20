# Aarstiderne Business Analytics (Power BI)

Repo til fælles arbejde på Aarstiderne-analysen i Power BI.

## Projektfiler (Power BI)

Power BI projektet ligger her:

- `powerbi/Aarstiderne-business-analytics.pbip`

Tilhørende artifacts:
- `powerbi/Aarstiderne-business-analytics.Report/`
- `powerbi/Aarstiderne-business-analytics.SemanticModel/`

## Hurtig start

1. Klon repo
2. Sæt lokal data-path med script
3. Åbn `.pbip`

Se guide:
- [`docs/powerbi-setup.md`](docs/powerbi-setup.md)

## Samarbejde (branches + async workflow)

Se branch-strategi og PR-flow:
- [`docs/samarbejde-git-workflow.md`](docs/samarbejde-git-workflow.md)

## Hurtige dataindsigter

- **Kunder:** 4.391
- **Ordrer:** 199.083
- **Faktura-linjer:** 199.083 (1:1 med ordre)
- **Hændelser:** 696.495
- **Datoperiode:** 2020-01-31 til 2022-07-25
- **Omsætning (fakturapris):** 121.826.938
- **Samlet rabat:** 1.197.756 (~0,97% af vejl. pris)

## Datamodel og visualiseringer

- Datamodel: [`docs/powerbi-datamodel.md`](docs/powerbi-datamodel.md)
- Visualiseringer: [`docs/visualiseringer.md`](docs/visualiseringer.md)
- DAX-forslag: [`docs/dax-measures.md`](docs/dax-measures.md)
- Profiling summary: [`docs/profiling-summary.md`](docs/profiling-summary.md)

## Scripts

- `scripts/validate_data_model.py` – valider relationer/datoer
- `scripts/set_powerbi_data_paths.py` – sæt datakilde-paths for teamet

Eksempel:

```bash
python scripts/set_powerbi_data_paths.py --data-dir "C:\Users\<dig>\Downloads"
python scripts/validate_data_model.py
```

## Datafiler

CSV-filer er ikke committet. Læg dem lokalt og peg modellen mod din mappe.

Se: `data/README.md`
