# Milestone-2

Part 2 : Source Code Mapping

## Purpose
This document maps each **BeautifulSoup API function** used in **Milestone 1 (Tasks 1–8)** and **Milestone 2 Part 1** to its corresponding implementation inside the original `bs4` source code.  
All line numbers refer to the **unmodified BeautifulSoup code** distributed with `beautifulsoup.zip`, prior to any modifications.  
The goal is to demonstrate understanding of how the high-level BeautifulSoup APIs correspond to their internal implementations.

---

## Source Code Reference Table

| API Function              | Source File        | Approx. Line No. | Description                                                                                      |
|----------------------------|--------------------|------------------:|--------------------------------------------------------------------------------------------------|
| `BeautifulSoup.__init__`  | `bs4/__init__.py`  |             ~209 | Initializes the BeautifulSoup object, sets up the parser, and builds the DOM tree.               |
| `prettify()`              | `bs4/element.py`   |            ~2601 | Formats and returns the parsed HTML tree as a neatly indented string.                            |
| `find_all()`              | `bs4/element.py`   |            ~2245 | Core search API that locates all tags matching the given name or attributes.                     |
| `find()`                  | `bs4/element.py`   |            ~2684 | Returns the first tag that matches specified criteria (single-tag search).                       |
| `find_parent()`           | `bs4/element.py`   |             ~992 | Retrieves the closest ancestor tag that matches a provided name or filter.                       |
| `select()`                | `bs4/element.py`   |            ~2799 | Executes CSS selector queries and returns all matching tags (via SoupSieve).                     |
| `get()`                   | `bs4/element.py`   |            ~2160 | Returns the value of an attribute for the current tag.                                           |
| `.get`                    | `bs4/element.py`   |            ~2185 | Retrieves a tag’s name or attribute value such as `id` or `href`.                                |
| `get_text()`              | `bs4/element.py`   |             ~524 | Concatenates and returns all descendant text nodes within a tag.                                 |
| `.name`                   | `bs4/element.py`   |             ~160 | Stores or retrieves the tag’s name (e.g., `div`, `p`).                                           |
| `attrs`                   | `bs4/element.py`   |             ~750 | Dictionary maintaining all tag attributes; assignment (`tag["class"] = …`) updates this mapping.  |
| `str(soup)`               | `bs4/element.py`   |            ~2302 | Converts the parse tree to HTML text via `decode()` (`__str__ = __unicode__ = __repr__`).         |

---

## Methodology
1. Opened the `bs4` source directory in VS Code.  
2. Used **Find in Files** (`Cmd + Shift + F`) 
3. Verified each API’s behavior by reviewing its docstring and implementation context.  
4. Recorded the file name, approximate line number, and a concise functional description.

---

## Summary
This mapping covers every BeautifulSoup function invoked in Milestone 1 and 2 Part 1, including:

- **Initialization / Parsing:** `BeautifulSoup.__init__`  
- **DOM Traversal & Search:** `find_all()`, `find()`, `find_parent()`, `select()`  
- **Attribute & Text Access:** `get()`, `attrs`, `name`, `get_text()`  
- **Output Serialization:** `prettify()`, `str(soup)`

Together, these APIs illustrate how BeautifulSoup encapsulates HTML parsing, searching, and serialization within a concise and expressive Python interface.