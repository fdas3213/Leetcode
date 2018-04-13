#use of stack data structure could be better
def isValid(s):
	symbols = "()[]{}"
	i = 0
	stop = False

	while not stop and i <len(s):
		if s[i+1] != symbols[symbols.index(s[i]) + 1]:
			stop = True
		i += 2

	return not stop

def isValid(s):
	symbols = {")":"(","]":"[","}":"{"}
	stack = []

	for char in s:
		if char in symbols.values():
			stack.append(char)

		elif char in symbols.keys():
			if stack == [] or symbols[char] != stack.pop():
				return False

		else:
			return False

	return stack == []
