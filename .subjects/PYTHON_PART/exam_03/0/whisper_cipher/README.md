# whisper_cipher

**Expected files:** `whisper_cipher.py`

**Allowed functions:** Built-in Python functions

---

## Description

Write a function that creates a simple cipher by shifting letters in a string by a given amount.
Non-alphabetic characters should not be changed.

Your function must be declared as follows:

```python
def whisper_cipher(text: str, shift: int) -> str:
```

### Examples

```
whisper_cipher("Hello, World!", 3)  => "Khoor, Zruog!"
whisper_cipher("Abz", 3)            => "Dec"
whisper_cipher("WXYZ 1", 1)         => "YZAB 1"
whisper_cipher("abc", 0)            => "abc"
```
