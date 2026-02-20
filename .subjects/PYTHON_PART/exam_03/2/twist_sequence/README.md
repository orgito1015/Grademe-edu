# twist_sequence

**Expected files:** `twist_sequence.py`

**Allowed functions:** All Python built-in functions

---

## Description

Write a function that rotates an array to the right by k positions.

The function should:
- Handle empty arrays
- Handle k values larger than the array length using modulo
- Rotate elements so the last k elements move to the front

Your function must be declared as follows:

```python
def twist_sequence(arr: list[int], k: int) -> list[int]:
```

## Example

```python
twist_sequence([1, 2, 3, 4, 5], 2)  # Returns: [4, 5, 1, 2, 3]
twist_sequence([1, 2, 3], 5)  # Returns: [2, 3, 1] (k % 3 = 2)
twist_sequence([], 3)  # Returns: []
```
