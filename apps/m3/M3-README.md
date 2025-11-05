# Milestone-3
 Milestone 3 — Transformer-Based SoupReplacer

## Overview
Milestone 3 extends the `SoupReplacer` API introduced in Milestone 2.  
Previously, transformations were limited to static string replacements (`<b>` → `<strong>`).  
Now, Milestone 3 integrates transformation logic directly into BeautifulSoup’s parsing flow —  
allowing live, dynamic tag and attribute modifications during parsing.  
This makes the replacer more powerful, extensible, and efficient.

---

## What Was Implemented

### 1. Transformer-Based `SoupReplacer`
`SoupReplacer` now accepts three optional transformer callables:
- **`name_xformer(tag)`** → modifies the tag name (e.g., rename `<b>` → `<blockquote>`).
- **`attrs_xformer(tag)`** → modifies or filters attributes (e.g., remove `class`, add `data-*`).
- **`xformer(tag)`** → applies arbitrary side effects directly on the tag object.

---

### 2. Parser Integration
`BeautifulSoup` was patched to accept a new keyword argument `replacer=SoupReplacer(...)`.  
The `HTMLParserTreeBuilder` applies this replacer automatically on each tag *as it is parsed*,  
so transformations happen in one pass — no need to re-parse HTML text.

---

### 3. Backward Compatibility
Milestone 2-style initialization is still supported:
```python
SoupReplacer("b", "strong")
```
This ensures older code and test cases continue to run unchanged.

---

### 4. Unit Testing
File: `bs4/tests/test_soupreplacer_m3.py`  
Tests validate:
- Tag renaming  
- Attribute addition/removal  
- Combined transformation logic  
- Legacy API compatibility  
- Replacer integration during parsing  

**All six tests passed successfully.**

---

### 5. Application — Task 7 (Updated)
Task 7 was reimplemented using the new live-transformation API.  
It dynamically adds or replaces `class="test"` on all `<p>` tags while parsing.

```python
def add_p_class(tag):
    if tag.name == "p":
        tag.attrs["class"] = "test"

replacer = SoupReplacer(xformer=add_p_class)
soup = BeautifulSoup(html, "html.parser", replacer=replacer)
```

Output file:  
`input.html.pclass.html`

---

## Comparison — Milestone 2 vs Milestone 3

In **Milestone 2**, transformations were performed by string replacement before parsing.  
This worked for simple cases but was limited and inefficient.  
We could rename tags, but not modify attributes or apply logic while parsing.  
Each change required two stages — text manipulation and re-parsing.

**Milestone 3** introduces dynamic, parser-level transformations.  
Each tag is intercepted during parsing and passed to `SoupReplacer` for modification.  
This design is faster, cleaner, and more flexible — enabling complex changes like  
conditional renames, selective attribute filtering, and chained operations.  
M3 also integrates seamlessly into the BeautifulSoup API and ensures backward compatibility.  

In summary:
- **M2** → Static string replacement before parsing.  
- **M3** → Live programmable transformations during parsing.  
- **Benefit** → Greater control, one-pass execution, and reusability for custom sanitizers or preprocessors.

---

## 💡 Recommendations
- Extend support for `lxml` and `html5lib` parsers.  
- Implement a `ReplacerPipeline` for chaining multiple transformations.  
- Add a verbose/debug mode to visualize tag transformation flow.  
- Package the replacer as a standalone plugin for community use.

---

## 🧪 How to Run

### Run Tests
```bash
PYTHONPATH=. python3 -m unittest bs4.tests.test_soupreplacer_m3 -v
```

Expected:
```
Ran 6 tests in 0.001s
OK
```

### Run Task 7 Application
```bash
PYTHONPATH=. python3 apps/m3/task7_soupreplacer.py apps/m3/input.html
```

Output example:
```
Updated <p> tags successfully. Wrote: apps/m3/input.html.pclass.html
```

---
