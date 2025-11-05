from bs4 import BeautifulSoup
from typing import Callable, Optional, Dict, Any

class SoupReplacer:
    """A class to facilitate tag and attribute transformations in BeautifulSoup."""
    def __init__(self,
                 og_tag: Optional[str] = None,
                 alt_tag: Optional[str] = None,
                 name_xformer: Optional[Callable] = None,
                 attrs_xformer: Optional[Callable] = None,
                 xformer: Optional[Callable] = None):
        """
        Initialize SoupReplacer with either:
        - (og_tag, alt_tag) for basic tag rename
        - or transformer functions for advanced tag/attribute manipulation
        """
        if og_tag and alt_tag:
            def pair_name_xformer(tag):
                return alt_tag if tag.name == og_tag else tag.name
            self.name_xformer = pair_name_xformer
        else:
            self.name_xformer = name_xformer

        self.attrs_xformer = attrs_xformer
        self.xformer = xformer
        self.og_tag = og_tag
        self.alt_tag = alt_tag

    def __call__(self, tag):
        """Apply transformations to a Tag object."""
        if not tag:
            return tag

        if callable(self.name_xformer):
            try:
                new_name = self.name_xformer(tag)
                if isinstance(new_name, str) and new_name:
                    tag.name = new_name
            except Exception:
                pass

        if callable(self.attrs_xformer):
            try:
                new_attrs = self.attrs_xformer(tag)
                if isinstance(new_attrs, dict):
                    tag.attrs = new_attrs
            except Exception:
                pass

        if callable(self.xformer):
            try:
                self.xformer(tag)
            except Exception:
                pass

        return tag

    def replace_tags(self, html: str) -> str:
        """Return modified HTML string with simple tag replacements."""
        if not self.og_tag or not self.alt_tag:
            raise ValueError("SoupReplacer not initialized with og_tag and alt_tag.")
        html = html.replace(f"<{self.og_tag}>", f"<{self.alt_tag}>")
        html = html.replace(f"</{self.og_tag}>", f"</{self.alt_tag}>")
        return html

    def parse(self, html: str, parser: str = "html.parser") -> BeautifulSoup:
        """
        Parse the HTML after performing replacements (Milestone-2 style).
        For advanced use, pass this replacer directly to BeautifulSoup:
            BeautifulSoup(html, 'html.parser', replacer=my_replacer)
        """
        if self.og_tag and self.alt_tag:
            replaced_html = html.replace(f"<{self.og_tag}>", f"<{self.alt_tag}>")
            replaced_html = replaced_html.replace(f"</{self.og_tag}>", f"</{self.alt_tag}>")
            return BeautifulSoup(replaced_html, parser)
        return BeautifulSoup(html, parser, replacer=self)