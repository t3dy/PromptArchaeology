"""
Build the Promptarchaeology-Heldscalla static site into docs/ for GitHub Pages.

Renders:
- index.html  (cute landing)
- narrative.html
- docs.html (index of project docs: README, CLAUDE.md, NARRATIVE.md)
- queries.html (catalog of saved SQL queries with syntax highlight)
- code.html (Python code listings)
- manuscripts.html (workspace .md files copied into manuscripts/)
- one HTML per markdown file
- one HTML per SQL or Python file (as code page)

Usage:
    python tools/build_site.py
"""
import sys
import shutil
import pathlib
import re
import html
import datetime as dt
import markdown

ROOT = pathlib.Path(__file__).resolve().parent.parent
SITE = ROOT / "site"
DOCS = ROOT / "docs"
TEMPLATE = (SITE / "template.html").read_text(encoding="utf-8")

MD_EXT = ["fenced_code", "tables", "toc"]


def render_markdown(md_text: str) -> str:
    return markdown.markdown(md_text, extensions=MD_EXT)


def page(title: str, content_html: str, depth: int = 0) -> str:
    root_prefix = "../" * depth if depth else ""
    return TEMPLATE.replace("{title}", html.escape(title)) \
                   .replace("{root}", root_prefix) \
                   .replace("{content}", content_html)


def write_page(out_path: pathlib.Path, title: str, content_html: str):
    depth = len(out_path.relative_to(DOCS).parts) - 1
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(page(title, content_html, depth), encoding="utf-8")


def code_block(code: str, lang: str = "") -> str:
    return f"<pre><code class=\"language-{lang}\">{html.escape(code)}</code></pre>"


def slugify(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", text.lower()).strip("_")


def render_index() -> str:
    """The cute landing page."""
    return """
<div class="hero">
  <h1>Heldscalla</h1>
  <p class="sub">Promptarchaeology — distant reading of one's own prompt history</p>
  <div class="epigraph">
    "He raised the broken pot and considered it. He did not know if Heldscalla itself
    would rise. He kept working anyway."
    <cite>— gloss on <em>Galactic Pot-Healer</em>, Philip K. Dick, 1969</cite>
  </div>
</div>

<p>This is a tool that reads <strong>only the user's prompts</strong> across
1.45M LLM messages and 5,271 conversations, ignoring the AI's outputs. The
methodological commitment is intentional: the user's writing lives in their
prompts; the output is a function of the AI's training. To study the user's
evolving thinking and values, study only the prompts.</p>

<p>The corpus is Heldscalla — sunken, partially indexed, organized by accident.
This tool is the craft of pot-healing: bringing one cascade or pattern at a
time into the light.</p>

<div class="section-title">Surfaces</div>
<div class="cards">
  <a class="card" href="coach.html">
    <div class="card-label">Coach</div>
    <h3>Glimmung-companion</h3>
    <p>Cards, openers, challenges, questions. Low-pressure forever.</p>
  </a>
  <a class="card" href="narrative.html">
    <div class="card-label">Lineage</div>
    <h3>Building on prior projects</h3>
    <p>From megabase to MTGSLIDER's Q-log convention to here.</p>
  </a>
  <a class="card" href="docs.html">
    <div class="card-label">Documentation</div>
    <h3>README, CLAUDE.md</h3>
    <p>How the tool is structured and how the agent navigates it.</p>
  </a>
  <a class="card" href="queries.html">
    <div class="card-label">Queries</div>
    <h3>Saved SQL incantations</h3>
    <p>Eleven ways of looking at a corpus of one's own writing.</p>
  </a>
  <a class="card" href="code.html">
    <div class="card-label">Code</div>
    <h3>Python &amp; schema</h3>
    <p>The runner, the chunker, the coach, the views over megabase.</p>
  </a>
  <a class="card" href="manuscripts.html">
    <div class="card-label">Manuscripts</div>
    <h3>Workshop documents</h3>
    <p>Tired-mode prompts, learning journal protocol, audit questions, and other planning artifacts.</p>
  </a>
</div>

<div class="water-line"></div>

<div class="section-title">The methodological move</div>
<p>Every prompt is a moment of intentional direction. Output is a function of the AI's
training distribution; the prompt is a function of you — your current framing, your
unspoken assumptions, your mood, the vocabulary that occurred to you under whatever
pressure. A pure prompt corpus is closer to unfiltered cognition than almost any
journal one might keep.</p>

<p>Crucially: <em>prompts that respond to outputs are the highest-signal artifacts in the
corpus.</em> When you write a follow-up, you've just been confronted with what your prompt
actually produced. Your reaction — redirect, clarify, push back, accept, pivot — is your
taste in real-time contact with output. Output-only analysis tells you what AI does.
Prompt-only analysis tells you what you reject and what you accept. The latter is closer
to <em>values</em> than almost anything else one could study.</p>

<div class="section-title">What lives below</div>
<ul>
  <li><strong>Megabase</strong> — the unified SQLite corpus across 11 sources (chats, SMS, Facebook, Twitter, PDF, gmail). 1.45M user prompts, 5,271 conversations.</li>
  <li><strong>The 1000-page cascades</strong> — Medieval Magic (1206 pp.), Atalanta Fugiens (988 pp.), Tilton on Spiritual Alchemy (892 pp.), Magic in Shakespeare (757 pp.). Book-length conversations on single topics.</li>
  <li><strong>The Q-log convention</strong> — verbatim user input as the artifact worth preserving (precursor convention from MTGSLIDER).</li>
</ul>
"""


def collect_files(*globs):
    paths = []
    for g in globs:
        paths.extend(sorted(ROOT.glob(g)))
    return paths


def main():
    if DOCS.exists():
        shutil.rmtree(DOCS)
    DOCS.mkdir()

    # copy CSS + favicon
    shutil.copy(SITE / "style.css", DOCS / "style.css")
    shutil.copy(SITE / "favicon.svg", DOCS / "favicon.svg")

    # 1) Index
    write_page(DOCS / "index.html", "Heldscalla", render_index())

    # 2) Narrative
    narrative_md = (ROOT / "NARRATIVE.md").read_text(encoding="utf-8")
    write_page(DOCS / "narrative.html", "Lineage", render_markdown(narrative_md))

    # 3) Docs index
    doc_files = [
        ("README.md", "README"),
        ("CLAUDE.md", "Agent Instructions (CLAUDE.md)"),
        ("NARRATIVE.md", "Lineage"),
    ]
    docs_links = "<ul>"
    for fname, title in doc_files:
        slug = slugify(fname.replace(".md", ""))
        out = DOCS / "doc" / f"{slug}.html"
        md_path = ROOT / fname
        if md_path.exists():
            write_page(out, title, render_markdown(md_path.read_text(encoding="utf-8")))
            docs_links += f'<li><a href="doc/{slug}.html">{html.escape(title)}</a></li>'
    docs_links += "</ul>"
    write_page(DOCS / "docs.html", "Documentation",
               f"<h1>Documentation</h1><p>Project-internal documents that explain how Heldscalla works and how the agent navigates it.</p>{docs_links}")

    # 4) Queries
    queries_html = ["<h1>Saved Queries</h1>",
                    "<p>Each <code>.sql</code> file is one way of looking at the corpus. The keyword filters are visible (so the queries reveal the analyst's interests) but the corpus content itself stays private.</p>",
                    "<ul>"]
    for sql_path in sorted((ROOT / "queries").glob("*.sql")):
        slug = sql_path.stem
        title = slug.replace("_", " ")
        sql_text = sql_path.read_text(encoding="utf-8")
        # Pull docstring from leading comments
        intro = "\n".join(line[3:].strip() for line in sql_text.splitlines() if line.startswith("--"))
        body = f"<h1>{html.escape(title)}</h1><p><em>From <code>queries/{sql_path.name}</code></em></p>"
        if intro:
            body += f"<blockquote>{html.escape(intro)}</blockquote>"
        body += code_block(sql_text, "sql")
        write_page(DOCS / "queries" / f"{slug}.html", title, body)
        queries_html.append(f'<li><a href="queries/{slug}.html">{html.escape(title)}</a></li>')
    queries_html.append("</ul>")
    write_page(DOCS / "queries.html", "Queries", "\n".join(queries_html))

    # 5) Code
    code_files = []
    for py_path in sorted((ROOT / "tools").glob("*.py")):
        code_files.append((py_path, "python"))
    for sql_path in sorted((ROOT / "schema").glob("*.sql")):
        code_files.append((sql_path, "sql"))

    code_html = ["<h1>Code</h1>", "<p>The runner, the cascade chunker, the schema views.</p>", "<ul>"]
    for path, lang in code_files:
        slug = slugify(f"{path.parent.name}_{path.stem}")
        content = path.read_text(encoding="utf-8")
        body = f"<h1>{html.escape(path.name)}</h1><p><em>{path.relative_to(ROOT).as_posix()}</em></p>" + code_block(content, lang)
        write_page(DOCS / "code" / f"{slug}.html", path.name, body)
        code_html.append(f'<li><a href="code/{slug}.html"><code>{html.escape(path.relative_to(ROOT).as_posix())}</code></a></li>')
    code_html.append("</ul>")
    write_page(DOCS / "code.html", "Code", "\n".join(code_html))

    # 6a) Coach
    coach_dir = ROOT / "coach"
    coach_links = [
        '<h1>Coach mode</h1>',
        '<p><em>Glimmung-companion. Low-pressure offerings — one card, one question, one challenge at a time. Never asks "did you ship?" Never recommends new projects. Always: follow your lead.</em></p>',
        '<p>Invoke from any Claude Code session: <code>coach me</code>, <code>give me a card</code>, <code>I&rsquo;m tired</code>, <code>ask me a question</code>.</p>',
        '<p>Or run directly:</p>',
        '<pre><code>python tools/coach.py                   # random pull from any pool\npython tools/coach.py --kind opener     # session opener\npython tools/coach.py --kind challenge  # bounded game\npython tools/coach.py --kind question   # Socratic question\npython tools/coach.py --kind card       # oblique strategy</code></pre>',
        '<h2>Pools</h2>',
        '<ul>',
    ]
    if coach_dir.exists():
        for md_path in sorted(coach_dir.glob("*.md")):
            slug = slugify(md_path.stem)
            title = md_path.stem.replace("_", " ").title()
            md_text = md_path.read_text(encoding="utf-8")
            body = render_markdown(md_text)
            write_page(DOCS / "coach" / f"{slug}.html", title, body)
            coach_links.append(f'<li><a href="coach/{slug}.html">{html.escape(title)}</a></li>')
    coach_links.append("</ul>")
    write_page(DOCS / "coach.html", "Coach", "\n".join(coach_links))

    # 6b) Manuscripts
    manu_dir = ROOT / "manuscripts"
    manu_links = ['<h1>Manuscripts</h1>',
                  '<p>Companion documents from the workshop sessions: tired-mode prompt libraries, learning-journal protocols, audit questions, project briefings, and other planning artifacts that orbit this tool.</p>',
                  "<ul>"]
    if manu_dir.exists():
        for md_path in sorted(manu_dir.glob("*.md")):
            slug = slugify(md_path.stem)
            title = md_path.stem.replace("_", " ")
            md_text = md_path.read_text(encoding="utf-8")
            body = render_markdown(md_text)
            write_page(DOCS / "manuscripts" / f"{slug}.html", title, body)
            manu_links.append(f'<li><a href="manuscripts/{slug}.html">{html.escape(title)}</a></li>')
    manu_links.append("</ul>")
    write_page(DOCS / "manuscripts.html", "Manuscripts", "\n".join(manu_links))

    # add .nojekyll so GitHub Pages serves underscored files
    (DOCS / ".nojekyll").write_text("", encoding="utf-8")

    print(f"built site at {DOCS}")
    print(f"  pages: {sum(1 for _ in DOCS.rglob('*.html'))}")


if __name__ == "__main__":
    main()
