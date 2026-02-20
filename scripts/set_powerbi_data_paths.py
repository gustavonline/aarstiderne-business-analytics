import argparse
import re
from pathlib import Path

TABLE_PATH = Path("powerbi") / "Aarstiderne-business-analytics.SemanticModel" / "definition" / "tables"

TABLE_FILE_TO_DATA_FILE = {
    "Geografi.tmdl": "Geografi.csv",
    "Hændelseslog.tmdl": "Hændelseslog.csv",
    "Kunder.tmdl": "Kunder.csv",
    "Ordrer.tmdl": "Ordrer.csv",
    "Produkter.tmdl": "Produkter.csv",
    "Faktura.tmdl": "faktura.csv",
}


def to_windows_path(raw: str) -> str:
    p = raw.strip()

    # Already windows-like
    if re.match(r"^[A-Za-z]:\\", p):
        return p.rstrip("\\/")

    # WSL/Git Bash style: /c/Users/... -> C:\Users\...
    m = re.match(r"^/([a-zA-Z])/(.*)$", p)
    if m:
        drive = m.group(1).upper()
        rest = m.group(2).replace("/", "\\")
        return f"{drive}:\\{rest}".rstrip("\\/")

    # fallback: just normalize separators
    return p.replace("/", "\\").rstrip("\\/")


def patch_file(path: Path, target_data_dir_win: str, expected_data_file: str) -> bool:
    text = path.read_text(encoding="utf-8")

    # Replace File.Contents(...) paths that point to the expected file
    pattern = re.compile(
        rf'File\.Contents\("[^"]*{re.escape(expected_data_file)}"\)',
        flags=re.IGNORECASE,
    )
    repl = f'File.Contents("{target_data_dir_win}\\{expected_data_file}")'

    new_text, count = pattern.subn(lambda _m: repl, text)

    if count > 0 and new_text != text:
        path.write_text(new_text, encoding="utf-8")
        return True

    return False


def main():
    parser = argparse.ArgumentParser(
        description="Opdater Power BI tmdl-kildepaths til en fælles data-mappe"
    )
    parser.add_argument(
        "--data-dir",
        required=True,
        help=r'Sti til mappe med CSV-filer, fx "C:\Users\gusta\Downloads"',
    )
    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parents[1]
    tables_dir = repo_root / TABLE_PATH

    if not tables_dir.exists():
        raise SystemExit(f"Kunne ikke finde tmdl-tabeller: {tables_dir}")

    data_dir_win = to_windows_path(args.data_dir)

    changed = []
    unchanged = []

    for table_file, data_file in TABLE_FILE_TO_DATA_FILE.items():
        p = tables_dir / table_file
        if not p.exists():
            unchanged.append(f"MISSING: {table_file}")
            continue

        if patch_file(p, data_dir_win, data_file):
            changed.append(table_file)
        else:
            unchanged.append(table_file)

    print("Data path root:", data_dir_win)
    print("Updated files:", len(changed))
    for f in changed:
        print("  -", f)

    if unchanged:
        print("Unchanged files:", len(unchanged))
        for f in unchanged:
            print("  -", f)

    print("\nTip: commit ændringerne, så teamet kan bruge samme path-konvention.")


if __name__ == "__main__":
    main()
