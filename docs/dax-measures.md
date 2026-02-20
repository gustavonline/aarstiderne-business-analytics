# DAX measures (forslag)

> Antager tabellerne hedder: `FactSalg`, `FactHændelse`, `DimKunde`, `DimDato`.

```DAX
Omsætning =
SUM ( FactSalg[fakturapris] )
```

```DAX
VejlPris =
SUM ( FactSalg[vejl_pris] )
```

```DAX
RabatBeløb =
[VejlPris] - [Omsætning]
```

```DAX
RabatPct =
DIVIDE ( [RabatBeløb], [VejlPris] )
```

```DAX
AntalOrdrer =
DISTINCTCOUNT ( FactSalg[Ordrenummer] )
```

```DAX
AntalKunder =
DISTINCTCOUNT ( FactSalg[kundenr] )
```

```DAX
AOV =
DIVIDE ( [Omsætning], [AntalOrdrer] )
```

```DAX
OrdrerPrKunde =
DIVIDE ( [AntalOrdrer], [AntalKunder] )
```

```DAX
AktiveKunder =
CALCULATE (
    DISTINCTCOUNT ( DimKunde[Kundenummer] ),
    DimKunde[status] = "aktiv"
)
```

```DAX
OmsætningYoY =
CALCULATE ( [Omsætning], SAMEPERIODLASTYEAR ( DimDato[Dato] ) )
```

```DAX
OmsætningYoY% =
DIVIDE ( [Omsætning] - [OmsætningYoY], [OmsætningYoY] )
```

```DAX
AntalHændelser =
COUNTROWS ( FactHændelse )
```

```DAX
AntalOpsigelser =
CALCULATE (
    [AntalHændelser],
    FactHændelse[hændelse] = "OPSIGELSE"
)
```

```DAX
AntalKundetilgange =
CALCULATE (
    [AntalHændelser],
    FactHændelse[hændelse] = "KUNDETILGANG"
)
```

```DAX
OpsigelsesRate =
DIVIDE ( [AntalOpsigelser], [AntalKundetilgange] )
```

## Ekstra (hvis du bruger timestamp-relation)

Hvis du har en inaktiv relation mellem `DimDato[Dato]` og `FactHændelse[timestamp_dato]`:

```DAX
AntalHændelserTimestamp =
CALCULATE (
    [AntalHændelser],
    USERELATIONSHIP ( DimDato[Dato], FactHændelse[timestamp_dato] )
)
```
