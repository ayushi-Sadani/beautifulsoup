import pytest
from bs4 import BeautifulSoup
from bs4 import Tag, NavigableString

def test_iter_simple_tag():
    soup = BeautifulSoup("<p>hello</p>", "html.parser")
    nodes = list(soup)
    # Expect: <p> and "hello"
    assert any(isinstance(n, Tag) and n.name == "p" for n in nodes)
    assert any(isinstance(n, NavigableString) and str(n) == "hello" for n in nodes)

def test_iter_nested_structure_order():
    html = "<div><p>Text <b>bold</b></p></div>"
    soup = BeautifulSoup(html, "html.parser")
    nodes = list(soup)

    div_i = next(i for i, n in enumerate(nodes) if isinstance(n, Tag) and n.name == "div")
    p_i   = next(i for i, n in enumerate(nodes) if isinstance(n, Tag) and n.name == "p")
    b_i   = next(i for i, n in enumerate(nodes) if isinstance(n, Tag) and n.name == "b")

    assert div_i < p_i < b_i

def test_iter_empty_document():
    soup = BeautifulSoup("", "html.parser")
    nodes = list(soup)
    assert nodes == []

def test_iter_text_only_document():
    soup = BeautifulSoup("Just text", "html.parser")
    nodes = list(soup)
    assert len(nodes) == 1
    assert isinstance(nodes[0], NavigableString)
    assert str(nodes[0]) == "Just text"

def test_iter_large_document():
    html = "<ul>" + "".join(f"<li>Item {i}</li>" for i in range(50)) + "</ul>"
    soup = BeautifulSoup(html, "html.parser")
    nodes = list(soup)

    # Expect exactly 50 <li> tags
    assert sum(1 for n in nodes if isinstance(n, Tag) and n.name == "li") == 50