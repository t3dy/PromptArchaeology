"""
Coach mode — pick a random offering for a tired session.

Usage:
    python tools/coach.py                   # random pull from any pool
    python tools/coach.py --kind opener     # session opener
    python tools/coach.py --kind challenge  # bounded game
    python tools/coach.py --kind question   # Socratic question
    python tools/coach.py --kind card       # oblique strategy
    python tools/coach.py --list            # list pool sizes
"""
import sys
import random
import re
import pathlib

# Windows consoles default to cp1252 and choke on the ❦ glyph; force UTF-8.
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

ROOT = pathlib.Path(__file__).resolve().parent.parent
COACH = ROOT / "coach"

POOLS = {
    "opener":    ("SESSION_OPENERS.md", "an opener"),
    "challenge": ("CHALLENGES.md",      "a challenge"),
    "question":  ("QUESTIONS.md",       "a question"),
    "card":      ("CARDS.md",           "a card"),
}


def parse_items(path: pathlib.Path):
    """Pull numbered or bulleted items from a markdown file (skip headers and prose)."""
    items = []
    for line in path.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^\s*(?:\d+\.|\-|\*)\s+(.+?)\s*$", line)
        if not m:
            continue
        item = m.group(1).strip()
        if not item or item.startswith("#"):
            continue
        items.append(item)
    return items


def pick(kind=None):
    if kind is None:
        kind = random.choice(list(POOLS))
    fname, label = POOLS[kind]
    path = COACH / fname
    if not path.exists():
        raise SystemExit(f"missing pool: {path}")
    items = parse_items(path)
    if not items:
        raise SystemExit(f"no items in {path}")
    return kind, label, random.choice(items)


def list_pools():
    print()
    for kind, (fname, label) in POOLS.items():
        path = COACH / fname
        n = len(parse_items(path)) if path.exists() else 0
        print(f"  {kind:10s}  {n:3d} items  ({fname})")
    print()


def main():
    args = sys.argv[1:]
    if "--list" in args:
        list_pools()
        return
    kind = None
    if "--kind" in args:
        idx = args.index("--kind")
        if idx + 1 >= len(args):
            raise SystemExit("--kind requires a value")
        kind = args[idx + 1]
        if kind not in POOLS:
            raise SystemExit(f"--kind must be one of {list(POOLS)}")
    k, label, item = pick(kind)
    print()
    print(f"  ❦  Heldscalla offers {label}:")
    print()
    # Wrap long lines for readability
    width = 76
    words = item.split()
    line = "  "
    for word in words:
        if len(line) + len(word) + 1 > width:
            print(line)
            line = "  " + word
        else:
            line += (" " if line.strip() else "") + word
    if line.strip():
        print(line)
    print()


if __name__ == "__main__":
    main()
