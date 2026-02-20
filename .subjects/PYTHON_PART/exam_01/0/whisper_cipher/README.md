# whisper_cipher

**Expected files:** `whisper_cipher.py`

**Allowed functions:** All Python built-in functions

---

## Description

Write a function that implements a Caesar cipher to shift alphabetic characters in a string.

The function should:
- Shift lowercase letters within the a-z range
- Shift uppercase letters within the A-Z range
- Keep non-alphabetic characters unchanged

Your function must be declared as follows:

```python
def whisper_cipher(text: str, shift: int) -> str:
```

## Example

```python
whisper_cipher("abc", 1)  # Returns: "bcd"
whisper_cipher("Hello World!", 3)  # Returns: "Khoor Zruog!"
whisper_cipher("xyz", 3)  # Returns: "abc"
```
