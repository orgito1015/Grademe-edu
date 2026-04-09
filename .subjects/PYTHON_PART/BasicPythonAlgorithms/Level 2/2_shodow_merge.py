def shadow_merge(list1: list[int], list2: list[int]) -> list[int]:
	merged = []
	for i in range(max(len(list1), len(list2))):
		if i < len(list1):
			merged.append(list1[i])
		if i < len(list2):
			merged.append(list2[i])
	return merged

# Example usage:
print(shadow_merge([1, 2, 3], [4, 5, 6]))  # Output: [1, 4, 2, 5, 3, 6]
print(shadow_merge([1, 2], [3, 4, 5, 5, 4, 3, 2, 1]))  # Output: [1, 3, 2, 4, 5, 5, 4, 3, 2, 1]