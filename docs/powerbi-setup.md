# Power BI setup (åbn projektet korrekt)

## Hvor ligger projektfilerne?

Åbn denne fil i Power BI Desktop:

- `powerbi/Aarstiderne-business-analytics.pbip`

> Brug **PBIP** (ikke `.pbix`) når I samarbejder i Git.

---

## 1) Klon repo

```bash
git clone https://github.com/gustavonline/aarstiderne-business-analytics.git
cd aarstiderne-business-analytics
```

## 2) Sørg for datafiler lokalt

Du skal have disse filer et sted lokalt:

- `Geografi.csv`
- `Hændelseslog.csv`
- `Ordrer.csv`
- `Produkter.csv`
- `faktura.csv`
- `Kunder.csv`

## 3) Sæt data-path i semantic model

Projektet bruger filkilder i Power Query (`File.Contents(...)`).

Sæt din egen data-mappe med scriptet:

```bash
python scripts/set_powerbi_data_paths.py --data-dir "C:\Users\<dig>\Downloads"
```

Eksempel:

```bash
python scripts/set_powerbi_data_paths.py --data-dir "C:\Data\Aarstiderne"
```

## 4) Valider datamodellen

```bash
python scripts/validate_data_model.py
```

## 5) Åbn i Power BI

1. Åbn `powerbi/Aarstiderne-business-analytics.pbip`
2. Klik **Refresh**
3. Hvis du får prompt om datakilder: godkend lokal filadgang

---

## Fejlsøgning

### “File not found”
Kør `set_powerbi_data_paths.py` igen med korrekt mappe.

### Æ/Ø/Å ser mærkeligt ud i terminal
Det er terminal-encoding og påvirker normalt ikke selve Power BI-modellen.

### Git viser lokale ændringer i `.pbi`/cache
Det skal ikke ske i dette repo (de er ignoreret). Hvis det sker, så commit dem ikke.
