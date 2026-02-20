# Power BI datamodel (anbefalet)

## 1) Tabeller og korn

## Faktatabeller

### `FactSalg` (ordre-korn: 1 række pr. ordre)
Byg denne ved at merge:

- `Ordrer[Ordrenummer]`
- `faktura[(FK)Ordrenummer]`

Behold fx felter:

- Dato: `dato`
- Kunde: `kundenr`
- Produkt: `produktnr`
- Geografi: `postnr_kunde`
- Drift: `rute`, `leveringstidspunkt`
- Pakke: `maddage`, `kuverter`
- Kampagne: `kampagne`, `rabatkode`, `rabatsats`
- Pris: `vejl_pris`, `fakturapris`

### `FactHændelse` (event-korn)
Direkte fra `Hændelseslog.csv`.

Vigtige felter:

- `timestamp` (datetime)
- `leveringsdato` (date, kan være tom)
- `kundenr`
- `ordrenr` (kan være tom ved abonnements-events)
- `kategori`
- `hændelse`

## Dimensioner

- `DimKunde` fra `Kunder.csv`
- `DimProdukt` fra `Produkter.csv`
- `DimGeografi` fra `Geografi.csv`
- `DimDato` (kalender)

---

## 2) Relationer

Brug **single direction** fra dimension -> fakta.

- `DimKunde[Kundenummer] 1 -> * FactSalg[kundenr]`
- `DimKunde[Kundenummer] 1 -> * FactHændelse[kundenr]`
- `DimProdukt[Produkternummer] 1 -> * FactSalg[produktnr]`
- `DimGeografi[Postnummer] 1 -> * DimKunde[postnr]`
- `DimDato[Dato] 1 -> * FactSalg[dato]`
- `DimDato[Dato] 1 -> * FactHændelse[leveringsdato]` (aktiv)
- `DimDato[Dato] 1 -> * FactHændelse[timestamp_dato]` (inaktiv, til USERELATIONSHIP)

> Undgå dobbelt geografi-stier i første version (fx både via kunde og direkte til FactSalg), så modellen ikke bliver tvetydig.

---

## 3) Datatyper og power query tips

### `faktura[dato]`
- Dansk tekstformat, fx `9. maj 2022`.
- Konverter med locale `Danish (Denmark)`.

### Numeriske felter
Sæt som heltal/decimal:

- `vejl_pris`, `fakturapris`, `rabatsats`, `maddage`, `kuverter`, `rute`

### Nøglefelter
Konverter til heltal/text konsistent:

- Kunde: `Kundenummer`, `kundenr`, `(FK)kundenr`
- Ordre: `Ordrenummer`, `(FK)Ordrenummer`, `ordrenr`
- Produkt: `produktnr`, `(FK)produktnr`, `Produkternummer`

---

## 4) Datakvalitet (observeret)

- Alle centrale nøgle-relationer matcher 100% på unikke værdier.
- `Ordrer` og `faktura` er 1:1 på ordrenummer.
- 1 kunde (`13847`) findes uden ordre/faktura (men findes i hændelseslog).

---

## 5) Model-udvidelse (når basis virker)

- `DimKampagne` (fra `kampagne` + `rabatkode`)
- `DimRute` (rutegrupper og performance)
- Retentions-/cohort-tabeller (måned for første levering vs genkøb)
