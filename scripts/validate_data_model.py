import csv
import re
from pathlib import Path
from datetime import datetime

FILES = {
    "Geografi.csv": ";",
    "Kunder.csv": ";",
    "Ordrer.csv": ";",
    "Produkter.csv": ";",
    "Hændelseslog.csv": ";",
    "faktura.csv": ",",
}

DANISH_MONTHS = {
    "januar": 1,
    "februar": 2,
    "marts": 3,
    "april": 4,
    "maj": 5,
    "juni": 6,
    "juli": 7,
    "august": 8,
    "september": 9,
    "oktober": 10,
    "november": 11,
    "december": 12,
}


def clean(v):
    return "" if v is None else v.strip()


def to_int(v):
    v = clean(v)
    if not v:
        return None
    try:
        if "." in v:
            x = float(v)
            if x.is_integer():
                return int(x)
            return None
        return int(v)
    except Exception:
        return None


def parse_date(v):
    v = clean(v)
    if not v:
        return None
    for fmt in ["%Y-%m-%d", "%Y-%m-%d %H:%M:%S.%f", "%d-%m-%Y", "%d-%m-%Y %H:%M"]:
        try:
            return datetime.strptime(v, fmt)
        except Exception:
            pass
    return None


def parse_danish_date(v):
    v = clean(v)
    m = re.match(r"^(\d{1,2})\.\s*([A-Za-zæøåÆØÅ]+)\s+(\d{4})$", v)
    if not m:
        return None
    day = int(m.group(1))
    mon = m.group(2).lower()
    year = int(m.group(3))
    if mon not in DANISH_MONTHS:
        return None
    return datetime(year, DANISH_MONTHS[mon], day)


def resolve_path(name: str) -> Path:
    candidates = [
        Path(name),
        Path("data") / name,
        Path("..") / name,
        Path("..") / "data" / name,
    ]
    for p in candidates:
        if p.exists():
            return p
    raise FileNotFoundError(
        f"Kunne ikke finde {name}. Søgte i repo root, data/, ../ og ../data/."
    )


def read_set(path, sep, col, intify=False):
    out = set()
    with path.open("r", encoding="utf-8", newline="") as f:
        r = csv.DictReader(f, delimiter=sep)
        for row in r:
            v = clean(row.get(col, ""))
            if not v:
                continue
            if intify:
                n = to_int(v)
                if n is not None:
                    out.add(str(n))
            else:
                out.add(v)
    return out


def count_rows(path):
    with path.open("r", encoding="utf-8", newline="") as f:
        return sum(1 for _ in f) - 1


def date_range(path, sep, col, parser):
    mn = mx = None
    with path.open("r", encoding="utf-8", newline="") as f:
        r = csv.DictReader(f, delimiter=sep)
        for row in r:
            d = parser(row.get(col, ""))
            if not d:
                continue
            mn = d if mn is None or d < mn else mn
            mx = d if mx is None or d > mx else mx
    return mn, mx


def pct(src, tgt):
    if not src:
        return 0, 0, 0.0
    m = len(src & tgt)
    return m, len(src), 100 * m / len(src)


def main():
    paths = {name: resolve_path(name) for name in FILES}

    print("=== ROW COUNTS ===")
    for name in FILES:
        print(f"{name}: {count_rows(paths[name])}")

    geo_post = read_set(paths["Geografi.csv"], ";", "Postnummer", intify=True)
    kunder = read_set(paths["Kunder.csv"], ";", "Kundenummer", intify=True)
    kunder_post = read_set(paths["Kunder.csv"], ";", "postnr", intify=True)
    ordrer = read_set(paths["Ordrer.csv"], ";", "Ordrenummer", intify=True)
    ordrer_kunder = read_set(paths["Ordrer.csv"], ";", "kundenr", intify=True)
    ordrer_post = read_set(paths["Ordrer.csv"], ";", "postnr_kunde", intify=True)
    ordrer_prod = read_set(paths["Ordrer.csv"], ";", "produktnr")
    produkter = read_set(paths["Produkter.csv"], ";", "Produkternummer")
    faktura_ordrer = read_set(paths["faktura.csv"], ",", "(FK)Ordrenummer", intify=True)
    faktura_kunder = read_set(paths["faktura.csv"], ",", "(FK)kundenr", intify=True)
    faktura_prod = read_set(paths["faktura.csv"], ",", "(FK)produktnr")

    # Hændelseslog sets
    log_ordrer = set()
    log_kunder = set()
    with paths["Hændelseslog.csv"].open("r", encoding="utf-8", newline="") as f:
        r = csv.DictReader(f, delimiter=";")
        for row in r:
            o = to_int(row.get("ordrenr", ""))
            c = to_int(row.get("kundenr", ""))
            if o is not None:
                log_ordrer.add(str(o))
            if c is not None:
                log_kunder.add(str(c))

    print("\n=== RELATION COVERAGE ===")
    checks = [
        ("Ordrer.kundenr -> Kunder.Kundenummer", ordrer_kunder, kunder),
        ("Ordrer.postnr_kunde -> Geografi.Postnummer", ordrer_post, geo_post),
        ("Kunder.postnr -> Geografi.Postnummer", kunder_post, geo_post),
        ("Ordrer.produktnr -> Produkter.Produkternummer", ordrer_prod, produkter),
        ("faktura.(FK)Ordrenummer -> Ordrer.Ordrenummer", faktura_ordrer, ordrer),
        ("faktura.(FK)kundenr -> Kunder.Kundenummer", faktura_kunder, kunder),
        ("faktura.(FK)produktnr -> Produkter.Produkternummer", faktura_prod, produkter),
        ("Hændelseslog.ordrenr -> Ordrer.Ordrenummer", log_ordrer, ordrer),
        ("Hændelseslog.kundenr -> Kunder.Kundenummer", log_kunder, kunder),
    ]
    for name, src, tgt in checks:
        m, n, p = pct(src, tgt)
        print(f"{name}: {m}/{n} ({p:.2f}%)")

    print("\n=== DATE RANGES ===")
    ord_mn, ord_mx = date_range(paths["Ordrer.csv"], ";", "dato", parse_date)
    kun_mn, kun_mx = date_range(paths["Kunder.csv"], ";", "oprettet_tmsp", parse_date)
    fak_mn, fak_mx = date_range(paths["faktura.csv"], ",", "dato", parse_danish_date)
    log_mn, log_mx = date_range(paths["Hændelseslog.csv"], ";", "timestamp", parse_date)

    f = lambda d: d.strftime("%Y-%m-%d") if d else "N/A"
    print("Ordrer.dato:", f(ord_mn), "->", f(ord_mx))
    print("Kunder.oprettet_tmsp:", f(kun_mn), "->", f(kun_mx))
    print("faktura.dato:", f(fak_mn), "->", f(fak_mx))
    print("Hændelseslog.timestamp:", f(log_mn), "->", f(log_mx))


if __name__ == "__main__":
    main()
