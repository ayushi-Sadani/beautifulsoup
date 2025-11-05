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

## Milestone-2 vs Milestone-3 — Comparison

| Aspect | Milestone-2 | Milestone-3 |
|--------|--------------|-------------|
| **Purpose** | Simple tag replacement | Dynamic transformation during parsing |
| **Usage** | `SoupReplacer("b", "blockquote")` | `SoupReplacer(name_xformer=..., attrs_xformer=..., xformer=...)` |
| **Flexibility** | Only replaces one tag name | Can change tag names, edit/remove attributes, and perform custom logic |
| **Integration** | Replacement done after parsing | Replacement happens live during parsing |
| **Scalability** | Limited to one-to-one replacement | Works with multiple tag types and complex logic |
| **Use-case Example** | Replace `<b>` with `<blockquote>` | Remove `class` attributes or rename `<i>` → `<em>` dynamically |

---

## Recommendations & Learnings (Student Perspective)

From working on Milestone-3, I realized how much power can come from letting users inject **functions** directly into the parsing process.  
While Milestone-2 was simple and useful for basic replacements, this new design makes `SoupReplacer` far more reusable — it can handle attribute clean-ups, tag renames, and even content annotations automatically.  

If I were to suggest improvements for future versions:
- I’d make it easier to **chain multiple replacers** together so different transformations can be composed.
- Adding **regex-based matching** for tag names or attributes could make it even more flexible.
- It might also be interesting to support **replacer pipelines**, where one replacer’s output becomes another’s input.

Overall, Milestone-3 felt like a big step toward turning `SoupReplacer` into something that could be merged into BeautifulSoup itself. It’s more Pythonic, customizable, and demonstrates a real example of extending open-source libraries cleanly.

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
