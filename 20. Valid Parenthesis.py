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
