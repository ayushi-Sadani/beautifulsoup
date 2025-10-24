"""
Task 6 — Using SoupReplacer
Rename all <b> tags to <blockquote> *during parsing* using the SoupReplacer API.
"""

import argparse, sys
from pathlib import Path
from bs4.soupreplacer import SoupReplacer

def pick_parser():
    try:
        import lxml
        return "lxml"
    except Exception:
        return "html.parser"

def main():
    ap = argparse.ArgumentParser(description="Rename all <b> tags to <blockquote> using SoupReplacer.")
    ap.add_argument("input_path", help="Path to HTML file")
    ap.add_argument("-o", "--out", help="Output file (defaults to <input>.replaced.html)")
    args = ap.parse_args()

    p = Path(args.input_path)
    if not p.exists():
        print(f"Error: file not found: {p}", file=sys.stderr)
        sys.exit(2)

    html_text = p.read_text(encoding="utf-8", errors="ignore")
    replacer = SoupReplacer("b", "blockquote")
    soup = replacer.parse(html_text, pick_parser())

    out = Path(args.out) if args.out else p.with_suffix(p.suffix + ".replaced.html")
    out.write_text(str(soup), encoding="utf-8")
    print(f"Replaced <b> tags with <blockquote>. Wrote: {out}")

if __name__ == "__main__":
    main()