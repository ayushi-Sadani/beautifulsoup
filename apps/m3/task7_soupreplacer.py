"""
Milestone 3 – Task 7 Re-implementation using SoupReplacer API
-------------------------------------------------------------
Find all <p> tags during parsing and set (or replace)
class="test", then write the transformed HTML to a file.
"""

import argparse, sys
from pathlib import Path
from bs4 import BeautifulSoup, SoupReplacer


def pick_parser():
    try:
        import lxml  # noqa
        return "lxml"
    except Exception:
        return "html.parser"


def p_class_transformer(tag):
    # Modify attributes only for <p> tags
    if tag.name == "p":
        new_attrs = dict(tag.attrs)
        new_attrs["class"] = ["test"]
        return new_attrs
    return tag.attrs


def main():
    ap = argparse.ArgumentParser(
        description='Add class="test" to all <p> tags using SoupReplacer.'
    )
    ap.add_argument("input_path")
    ap.add_argument("-o", "--out", help="Output file (defaults to <input>.pclass.html)")
    args = ap.parse_args()

    p = Path(args.input_path)
    if not p.exists():
        print(f"Error: {p} not found", file=sys.stderr)
        sys.exit(2)

    # Create replacer that sets class="test" for <p> tags
    replacer = SoupReplacer(attrs_xformer=p_class_transformer)

    with p.open("r", encoding="utf-8", errors="ignore") as f:
        html = f.read()
        soup = BeautifulSoup(html, pick_parser(), replacer=replacer)

    out = Path(args.out) if args.out else p.with_suffix(p.suffix + ".pclass.html")
    out.write_text(str(soup), encoding="utf-8")

    print(f'Processed "{p.name}": wrote updated HTML to "{out.name}".')


if __name__ == "__main__":
    main()