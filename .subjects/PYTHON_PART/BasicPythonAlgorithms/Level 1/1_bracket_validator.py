# write a function that checks if brackets braces and parenthesis are properly balanced and correctly nested in a string def bracket_validator(s:str) -> bool:

def bracket_validator(s: str) -> bool:
	stack = []
	pairs = {')': '(', '}': '{', ']': '['}
	
	for char in s:
		if char in pairs.values():
			stack.append(char)
		elif char in pairs.keys():
			if not stack or stack[-1] != pairs[char]:
				return False
			stack.pop()
	
	return len(stack) == 0