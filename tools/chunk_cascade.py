"""
Chunk a single large cascade into prompt-only markdown files.
Useful for the 1000-page conversations where the whole thing is too long to read at once.

Usage:
    python tools/chunk_cascade.py <conversation_id>
    python tools/chunk_cascade.py <conversation_id> --chunk-size 30

Outputs:
    reports/cascades/<title-slug>/chunk_NNN.md   — 50 prompts each by default
    reports/cascades/<title-slug>/TIMELINE.md    — index with date ranges
"""
import sys
import sqlite3
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
MEGABASE = pathlib.Path(r"C:\Dev\megabase\megabase.db")
VIEWS = ROOT / "schema" / "views.sql"


def slugify(text: str) -> str:
    s = re.sub(r"[^A-Za-z0-9]+", "_", text or "untitled").strip("_")
    return s[:60] or "untitled"


def chunk_cascade(conv_id: int, chunk_size: int = 50):
    uri = f"file:{MEGABASE.as_posix()}?mode=ro"
    conn = sqlite3.connect(uri, uri=True)
    conn.row_factory = sqlite3.Row
    conn.executescript(VIEWS.read_text(encoding="utf-8"))

    info = conn.execute(
        "SELECT conversation_title, source_name, prompt_count, estimated_pages "
        "FROM pa_cascades WHERE conversation_id = ?",
        (conv_id,),
    ).fetchone()
    if not info:
        raise SystemExit(f"no cascade with conversation_id={conv_id}")

    title = info["conversation_title"] or f"conv_{conv_id}"
    print(f"chunking: {title}  ({info['prompt_count']} prompts, {info['estimated_pages']:.0f} pages)")

    rows = conn.execute(
        "SELECT message_id, created_at, prompt_text, approx_words, reacts_to_output "
        "FROM pa_prompts WHERE conversation_id = ? ORDER BY message_id",
        (conv_id,),
    ).fetchall()

    out_dir = ROOT / "reports" / "cascades" / slugify(title)
    out_dir.mkdir(parents=True, exist_ok=True)

    timeline = [
        f"# Cascade: {title}",
        "",
        f"- conversation_id: `{conv_id}`",
        f"- source: `{info['source_name']}`",
        f"- total prompts: **{len(rows)}**",
        f"- estimated pages: **{info['estimated_pages']:.0f}**",
        f"- chunk size: {chunk_size}",
        "",
        "Legend: `▷` first turn, `↳` reacting to AI output.",
        "",
        "## Chunks",
        "",
    ]

    n_chunks = (len(rows) + chunk_size - 1) // chunk_size
    for chunk_idx in range(n_chunks):
        start = chunk_idx * chunk_size
        chunk_rows = rows[start:start + chunk_size]
        chunk_path = out_dir / f"chunk_{chunk_idx:03d}.md"
        lines = [
            f"# {title} — chunk {chunk_idx:03d}",
            "",
            f"Prompts {start + 1}–{start + len(chunk_rows)} of {len(rows)}.",
            "",
        ]
        for row in chunk_rows:
            ts = row["created_at"] or "(no timestamp)"
            marker = "↳" if row["reacts_to_output"] else "▷"
            lines.append(f"## {marker} {ts}  *({row['approx_words']} words)*")
            lines.append("")
            lines.append((row["prompt_text"] or "(empty)").rstrip())
            lines.append("")
            lines.append("---")
            lines.append("")
        chunk_path.write_text("\n".join(lines), encoding="utf-8")

        first_ts = (chunk_rows[0]["created_at"] or "?")[:10]
        last_ts = (chunk_rows[-1]["created_at"] or "?")[:10]
        timeline.append(f"- [chunk_{chunk_idx:03d}.md]({chunk_path.name}) — {first_ts} → {last_ts}")

    (out_dir / "TIMELINE.md").write_text("\n".join(timeline), encoding="utf-8")
    print(f"wrote {n_chunks} chunks + TIMELINE.md to {out_dir}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    cid = int(sys.argv[1])
    cs = 50
    if "--chunk-size" in sys.argv:
        cs = int(sys.argv[sys.argv.index("--chunk-size") + 1])
    chunk_cascade(cid, cs)
