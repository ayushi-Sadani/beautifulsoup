# Milestone 4 – Iterable BeautifulSoup

## Overview

Milestone 4 adds support for making the `BeautifulSoup` object directly iterable.
With this feature, users can loop through all nodes in the parsed HTML tree—tags, text nodes, and nested elements—simply by iterating over the `BeautifulSoup` instance.

This makes the library more Pythonic, improves usability, and avoids requiring manual access to `.descendants`.

---

## What Was Implemented

A new `__iter__` method was added to the `BeautifulSoup` class.

### Key Features
- Iterates through **all nodes** in document order  
- Uses the existing `.descendants` generator (efficient and memory-safe)  
- Does **not** build intermediate lists  
- Fully compatible with BeautifulSoup’s internal tree model  

### Code Added

```python
def __iter__(self):
    return self.descendants
```

### Example Usage

```python
from bs4 import BeautifulSoup

soup = BeautifulSoup("<p>Hello <b>World</b></p>", "html.parser")

for node in soup:
    print(node)
```

---

## How to Run

To run only the Milestone 4 test cases:

```bash
python3 -m pytest bs4/tests/test_milestone4_iteration.py
```

All 5 tests in this file pass correctly.
