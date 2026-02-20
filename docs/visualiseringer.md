# Visualiseringer til Power BI

## Side 1 – Executive overview

**Formål:** Hurtigt overblik over forretningen.

Visuals:
- KPI cards:
  - Omsætning
  - Antal ordrer
  - Antal kunder
  - Gns. ordre værdi
  - Rabat-%
- Linjegraf: omsætning pr. måned
- Kombinationsgraf: ordrer + omsætning pr. måned
- Donut: omsætning pr. region

God indsigt fra data:
- Omsætning topper i **maj 2022**.
- Dataperioden er 2020-02 til 2022-07.

---

## Side 2 – Produktperformance

**Formål:** Se hvilke kasser der driver volume og omsætning.

Visuals:
- Søjlediagram: antal ordrer pr. produkt
- Søjlediagram: omsætning pr. produkt
- 100% stacked bar: produktmix pr. region
- Matrix: produkt x maddage x kuverter

God indsigt fra data:
- Største produkter på volume: `562-12`, `287-32`, `934-33`.

---

## Side 3 – Geografi

**Formål:** Find regionale forskelle.

Visuals:
- Filled map: omsætning pr. region/landsdel
- Tabellenhed: postnr med omsætning og antal kunder
- Heatmap: region x produkt
- Slicer: status, produkt, kampagne

God indsigt fra data:
- Højeste omsætning i **Region Hovedstaden**.

---

## Side 4 – Kunde & abonnement

**Formål:** Forstå livscyklus og churn-signaler.

Visuals:
- Funnel: KUNDETILGANG -> PAUSE -> GENOPTAGET -> OPSIGELSE
- Linje: events over tid pr. hændelsestype
- Stacked bar: kundestatus pr. region
- Scatter: kunder (ordrer vs omsætning)

God indsigt fra data:
- Hændelseslog har meget stærke livscyklus-signaler til churn/retention analyse.

---

## Side 5 – Kampagne og rabat

**Formål:** Se effekt af kampagner på pris og volume.

Visuals:
- Søjlediagram: ordrer pr. kampagne
- Søjlediagram: samlet rabat pr. rabatkode
- Boxplot/kolonne: fakturapris med/uden rabat
- Decomposition tree: omsætning -> region -> produkt -> kampagne

God indsigt fra data:
- De fleste ordrer har ingen kampagne/rabat.
- `VELKOMMEN TILBAGE` og `VELKOMMEN50` står for stor del af rabatbeløb.
