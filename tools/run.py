"""
Run a saved query from queries/ against megabase.db (read-only) and write a markdown report.

Usage:
    python tools/run.py 01_first_prompts
    python tools/run.py 06
    python tools/run.py obsession

Partial matches accepted; the first matching .sql file wins.
"""
import sys
import sqlite3
import pathlib
import datetime as dt

ROOT = pathlib.Path(__file__).resolve().parent.parent
MEGABASE = pathlib.Path(r"C:\Dev\megabase\megabase.db")
VIEWS = ROOT / "schema" / "views.sql"
QUERIES = ROOT / "queries"
REPORTS = ROOT / "reports"


def open_db() -> sqlite3.Connection:
    if not MEGABASE.exists():
        raise FileNotFoundError(f"megabase.db not found at {MEGABASE}")
    uri = f"file:{MEGABASE.as_posix()}?mode=ro"
    conn = sqlite3.connect(uri, uri=True)
    conn.row_factory = sqlite3.Row
    # apply TEMP views every run; main DB stays read-only
    conn.executescript(VIEWS.read_text(encoding="utf-8"))
    return conn


def resolve_query(name: str) -> pathlib.Path:
    direct = QUERIES / f"{name}.sql"
    if direct.exists():
        return direct
    candidates = sorted(QUERIES.glob(f"*{name}*.sql"))
    if not candidates:
        raise FileNotFoundError(f"no query matching '{name}' in {QUERIES}")
    if len(candidates) > 1:
        names = "\n  ".join(c.name for c in candidates)
        print(f"multiple matches:\n  {names}\nusing: {candidates[0].name}")
    return candidates[0]


def run_query(name: str) -> pathlib.Path:
    sql_path = resolve_query(name)
    sql = sql_path.read_text(encoding="utf-8")
    conn = open_db()

    started = dt.datetime.now()
    cursor = conn.execute(sql)
    columns = [d[0] for d in cursor.description] if cursor.description else []
    rows = cursor.fetchall()
    elapsed = (dt.datetime.now() - started).total_seconds()

    REPORTS.mkdir(exist_ok=True)
    out = REPORTS / f"{dt.date.today().isoformat()}_{sql_path.stem}.md"
    out.write_text(format_markdown(sql_path.stem, columns, rows, elapsed, sql), encoding="utf-8")
    print(f"wrote {out} ({len(rows)} rows, {elapsed:.2f}s)")
    return out


def format_markdown(name, columns, rows, elapsed, sql):
    lines = [
        f"# {name}",
        "",
        f"_Run: {dt.datetime.now().isoformat(timespec='seconds')} | Rows: {len(rows)} | Elapsed: {elapsed:.2f}s_",
        "",
    ]
    if not rows:
        lines.append("No rows returned.")
    else:
        lines.append("| " + " | ".join(columns) + " |")
        lines.append("|" + "|".join("---" for _ in columns) + "|")
        for row in rows:
            cells = []
            for col in columns:
                val = row[col]
                if val is None:
                    cells.append("")
                else:
                    s = str(val).replace("|", "\\|").replace("\n", " ⏎ ").replace("\r", "")
                    cells.append(s)
            lines.append("| " + " | ".join(cells) + " |")
    lines.extend(["", "## Query", "", "```sql", sql.strip(), "```"])
    return "\n".join(lines)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    run_query(sys.argv[1])
