def sort_merge(list1: list[int], list2: list[int]) -> list[int]:
    return sorted(list1 + list2)

print(sort_merge([1, 3, 5], [2, 4, 3]))
print(sort_merge([1, 3, 5], [2, 4, 6]))  # Output: [1, 2, 3, 4, 5, 6]

