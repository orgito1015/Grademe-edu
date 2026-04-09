# cryptic_sort

**Expected files:** `cryptic_sort.py`

**Allowed functions:** Built-in Python functions

---

## Description

Write a function that sorts a list of strings by the following criteria (in order of priority):
1. Length of the string (shorter first)
2. Alphabetical order (case-insensitive)
3. Number of vowels (fewer vowels first)

Your function must be declared as follows:

```python
def cryptic_sort(strings: list) -> list:
```

### Examples

```
cryptic_sort(["A", "banana", "grape", "kiwi", "oArange"])  => ["A", "kiwi", "grape", "banana", "oArange"]
cryptic_sort(["a", "e", "b", "o", "u"])                    => ["a", "b", "e", "o", "u"]
cryptic_sort(["Arsen", "arsen", "ARSEN"])                   => ["ARSEN", "Arsen", "arsen"]
```
