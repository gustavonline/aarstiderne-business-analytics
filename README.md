# Aarstiderne Business Analytics (Power BI)

Dette repo er sat op til at hjælpe med datamodellering og visualisering i Power BI for følgende filer:

- `Geografi.csv`
- `Hændelseslog.csv`
- `Ordrer.csv`
- `Produkter.csv`
- `faktura.csv`
- (valgfri) `Kunder.csv` til kundedimension

## Hurtige dataindsigter

- **Kunder:** 4.391
- **Ordrer:** 199.083
- **Faktura-linjer:** 199.083 (1:1 med ordre)
- **Hændelser:** 696.495
- **Datoperiode:** 2020-01-31 til 2022-07-25
- **Omsætning (fakturapris):** 121.826.938
- **Samlet rabat:** 1.197.756 (~0,97% af vejl. pris)

## Anbefalet model (kort)

Byg en stjernemodel med 2 fakta-tabeller:

- `FactSalg` = merge af `Ordrer` + `faktura` på ordrenummer
- `FactHændelse` = `Hændelseslog`

Dimensioner:

- `DimKunde` (`Kunder.csv`)
- `DimProdukt` (`Produkter.csv`)
- `DimDato` (kalendertabel)
- `DimGeografi` (`Geografi.csv`)

Detaljer: se [`docs/powerbi-datamodel.md`](docs/powerbi-datamodel.md)

## Foreslåede rapport-sider

1. **Executive overview** (KPI’er + trends)
2. **Produktperformance** (mix, omsætning, kuverter/maddage)
3. **Geografi** (kort + region/landsdel)
4. **Kunde- og abonnementsadfærd** (pause/genoptag/opsigelse)
5. **Kampagne og rabat-effekt**

Detaljer: se [`docs/visualiseringer.md`](docs/visualiseringer.md)

## DAX-målinger

Forslag til centrale measures ligger i:

- [`docs/dax-measures.md`](docs/dax-measures.md)

## Datavalidering

Script til at validere nøgler og relationer:

- `scripts/validate_data_model.py`

Kør:

```bash
python scripts/validate_data_model.py
```

## Bemærk om datafiler

Repoet holder sig letvægts. Læg CSV-filerne i en lokal `data/` mappe eller peg Power BI direkte mod dine eksisterende filer.

Se: `data/README.md`
