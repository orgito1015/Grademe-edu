# cryptic_sorter

**Expected files:** `cryptic_sorter.py`

**Allowed functions:** All Python built-in functions

---

## Description

Write a function that sorts strings using the following criteria in order of priority:
1. By length (shortest first) — primary sort key
2. Alphabetically (case-insensitive) — secondary sort key, breaks ties in length
3. By number of vowels (ascending) — tertiary sort key, breaks ties in length and alphabetical order

The function should handle empty lists and count vowels (a, e, i, o, u) case-insensitively.

Your function must be declared as follows:

```python
def cryptic_sorter(strings: list[str]) -> list[str]:
```

## Example

```python
cryptic_sorter(["hello", "hi", "hey"])  # Returns: ["hi", "hey", "hello"]
# "hi" (len 2) < "hey" (len 3) < "hello" (len 5) — sorted by length (primary)

cryptic_sorter(["apple", "zoo", "bee"])  # Returns: ["zoo", "bee", "apple"]
# "zoo" (len 3, 1 vowel) < "bee" (len 3, 2 vowels) — same length, same alpha order tie broken by vowel count
# "apple" (len 5) comes last due to longer length

cryptic_sorter(["bat", "cat", "ant"])  # Returns: ["ant", "bat", "cat"]
# All length 3; "ant" < "bat" < "cat" alphabetically (secondary sort key)

cryptic_sorter([])  # Returns: []
```
