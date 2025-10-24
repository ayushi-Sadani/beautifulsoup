# -*- coding: utf-8 -*-
"""Tests for the custom SoupReplacer API."""

import pytest
from bs4.soupreplacer import SoupReplacer
from bs4 import BeautifulSoup


class TestSoupReplacer:
    """Test the SoupReplacer API that replaces tags during parsing."""

    def test_single_tag_replacement(self):
        """Verify that a single <b> tag is replaced with <blockquote>."""
        html = "<html><body><b>Hello World</b></body></html>"
        replacer = SoupReplacer("b", "blockquote")

        soup = replacer.parse(html)

        # Expected: <blockquote>Hello World</blockquote>
        assert soup.find("blockquote") is not None
        assert soup.find("b") is None
        assert soup.blockquote.text == "Hello World"
        # Ensure structure remains valid HTML
        assert isinstance(soup, BeautifulSoup)
        assert "<blockquote>" in str(soup)
        assert "</blockquote>" in str(soup)

    def test_multiple_tag_replacements(self):
        """Verify that multiple <b> tags are replaced with <strong>."""
        html = "<div><b>First</b> and <b>Second</b></div>"
        replacer = SoupReplacer("b", "strong")

        soup = replacer.parse(html)

        # Both <b> tags should now be <strong>
        strong_tags = soup.find_all("strong")
        assert len(strong_tags) == 2
        assert soup.find("b") is None
        assert strong_tags[0].text == "First"
        assert strong_tags[1].text == "Second"
        assert isinstance(soup, BeautifulSoup)