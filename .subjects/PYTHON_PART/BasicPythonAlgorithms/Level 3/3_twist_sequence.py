def twist_sequence(arr: list[int], k: int) -> list[int]:
    if not arr:
        return arr
    k = k % len(arr)
    return arr[-k:] + arr[:-k]

# Example usage:
print(twist_sequence([1, 2, 3, 4, 5], 2))  # Output: [4, 5, 1, 2, 3]
print(twist_sequence([1, 2, 3, 4, 5], 3))  # Output: [3, 4, 5, 1, 2]
print(twist_sequence([1, 2, 3, 4, 5], 5))  # Output: [1, 2, 3, 4, 5]