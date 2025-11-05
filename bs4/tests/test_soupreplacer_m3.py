import unittest
from bs4 import BeautifulSoup, SoupReplacer

print(">>> Running SoupReplacer M3 tests...")

HTML = """
<div class="wrap">
  <b class="x">hi</b>
  <p id="p1" class="lead">para <i>italics</i></p>
  <a href="/x" class="link">go</a>
</div>
"""

class TestSoupReplacerM3(unittest.TestCase):

    def test_name_xformer_basic(self):
        replacer = SoupReplacer(name_xformer=lambda t: "blockquote" if t.name == "b" else t.name)
        soup = BeautifulSoup(HTML, "html.parser", replacer=replacer)
        self.assertIsNone(soup.find("b"))
        self.assertIsNotNone(soup.find("blockquote"))

    def test_attrs_xformer_add_attribute(self):
        def add_attr(t):
            if t.name == "p":
                new_attrs = dict(t.attrs)
                new_attrs["data-role"] = "note"
                return new_attrs
            return t.attrs
        replacer = SoupReplacer(attrs_xformer=add_attr)
        soup = BeautifulSoup(HTML, "html.parser", replacer=replacer)
        self.assertEqual(soup.find("p")["data-role"], "note")

    def test_xformer_remove_class(self):
        def rm_class(t):
            if "class" in t.attrs:
                del t.attrs["class"]
        replacer = SoupReplacer(xformer=rm_class)
        soup = BeautifulSoup(HTML, "html.parser", replacer=replacer)
        self.assertIsNone(soup.find(attrs={"class": True}))

    def test_combined_transformers(self):
        def rename_i(t): return "em" if t.name == "i" else t.name
        def update_a(t):
            if t.name == "a":
                new_attrs = dict(t.attrs)
                new_attrs["rel"] = "nofollow"
                return new_attrs
            return t.attrs
        def add_suffix(t):
            if t.name == "p":
                t.attrs["id"] = t.attrs.get("id", "") + "_x"
        replacer = SoupReplacer(name_xformer=rename_i, attrs_xformer=update_a, xformer=add_suffix)
        soup = BeautifulSoup(HTML, "html.parser", replacer=replacer)
        self.assertIsNotNone(soup.find("em"))
        self.assertEqual(soup.find("a")["rel"], "nofollow")
        self.assertTrue(soup.find("p")["id"].endswith("_x"))

    def test_legacy_pair_constructor(self):
        replacer = SoupReplacer("b", "strong")
        soup = BeautifulSoup(HTML, "html.parser", replacer=replacer)
        self.assertIsNone(soup.find("b"))
        self.assertIsNotNone(soup.find("strong"))

    def test_runs_during_parsing(self):
        replacer = SoupReplacer(name_xformer=lambda t: "section" if t.name == "div" else t.name)
        soup = BeautifulSoup(HTML, "html.parser", replacer=replacer)
        section = soup.find("section")
        self.assertIsNotNone(section)
        self.assertIn("hi", section.get_text())

if __name__ == "__main__":
    unittest.main()