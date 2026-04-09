# sort_merge

**Expected files:** `sort_merge.py`

**Allowed functions:** Built-in Python functions

---

## Description

Write a function that merges two sorted lists of integers and returns a single sorted list.

Your function must be declared as follows:

```python
def sort_merge(list1: list, list2: list) -> list:
```

### Examples

```
sort_merge([1, 3, 5], [2, 4, 3])  => [1, 2, 3, 3, 4, 5]
sort_merge([1, 3, 5], [2, 4, 6])  => [1, 2, 3, 4, 5, 6]
sort_merge([], [1, 2, 3])         => [1, 2, 3]
sort_merge([5], [1])              => [1, 5]
```
