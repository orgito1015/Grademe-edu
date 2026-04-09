'''if two strings are permutations of each other, then they must have the same characters with the same frequency.'''
def string_permutation_checker(str1: str, str2: str) -> bool:
	# Remove whitespace and convert to lowercase
	str1 = str1.replace(" ", "").lower()
	str2 = str2.replace(" ", "").lower()
	
	# Check if the sorted characters of both strings are the same
	return sorted(str1) == sorted(str2)





# Example usage:
print(string_permutation_checker("listen", "silent"))  # Output: True
print(string_permutation_checker("hello", "world"))    # Output: False
print(string_permutation_checker("Triangle", "Integral"))  # Output: True