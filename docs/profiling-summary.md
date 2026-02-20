# Profiling summary af datasættet

## Datamængde

| Fil | Rækker |
|---|---:|
| Geografi.csv | 605 |
| Kunder.csv | 4.391 |
| Ordrer.csv | 199.083 |
| faktura.csv | 199.083 |
| Hændelseslog.csv | 696.495 |
| Produkter.csv | 7 |

## Datoperiode

- `Kunder.oprettet_tmsp`: **2020-01-31 -> 2022-07-24**
- `Ordrer.dato`: **2020-02-03 -> 2022-07-25**
- `faktura.dato`: **2020-02-03 -> 2022-07-25**
- `Hændelseslog.timestamp`: **2020-01-31 -> 2022-07-25**

## Relationstjek (unikke værdier)

- `Ordrer.kundenr -> Kunder.Kundenummer`: **100% match**
- `Ordrer.postnr_kunde -> Geografi.Postnummer`: **100% match**
- `Ordrer.produktnr -> Produkter.Produkternummer`: **100% match**
- `faktura.(FK)Ordrenummer -> Ordrer.Ordrenummer`: **100% match**
- `faktura.(FK)kundenr -> Kunder.Kundenummer`: **100% match**
- `faktura.(FK)produktnr -> Produkter.Produkternummer`: **100% match**
- `Hændelseslog.ordrenr -> Ordrer.Ordrenummer`: **100% match på udfyldte ordrenr**

Bemærkning:
- Kunde `13847` findes i kundetabellen, men har ingen ordre/faktura.

## Forretningsnøgletal (fra faktura)

- Samlet omsætning (`fakturapris`): **121.826.938**
- Samlet vejl. pris: **123.024.694**
- Samlet rabat: **1.197.756**
- Rabatandel: **0,97%**
- Gns. ordreomsætning: **611,94**

## Produkt- og regionshøjdepunkter

- Mest solgte produkter: `562-12`, `287-32`, `934-33`
- Højeste omsætning: **Region Hovedstaden**

## Hændelseslog (top)

- Kategorier:
  - LEVERING: 398.517
  - ØKONOMI: 199.083
  - ABONNEMENT: 98.895
- Vigtige hændelser:
  - ORDRE PAKKET: 199.083
  - FAKTURA: 199.083
  - LEVERET TIL KUNDE: 199.083
  - PAUSE: 34.442
  - OPSIGELSE: 10.168
