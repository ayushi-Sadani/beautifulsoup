from bs4 import BeautifulSoup

class SoupReplacer:
    """
    Replace all occurrences of a specified tag name during parsing.

    Example:
        replacer = SoupReplacer("b", "blockquote")
        soup = replacer.parse("<b>Hello</b>")
        print(soup)
    """

    def __init__(self, og_tag: str, alt_tag: str):
        self.og_tag = og_tag
        self.alt_tag = alt_tag

    def replace_tags(self, html: str) -> str:
        """Return a modified HTML string with the target tag replaced."""
        html = html.replace(f"<{self.og_tag}>", f"<{self.alt_tag}>")
        html = html.replace(f"</{self.og_tag}>", f"</{self.alt_tag}>")
        return html

    def parse(self, html: str, parser: str = "html.parser") -> BeautifulSoup:
        """Parse the HTML after performing replacements."""
        replaced_html = self.replace_tags(html)
        return BeautifulSoup(replaced_html, parser)