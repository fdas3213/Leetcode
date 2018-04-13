
def longestCommonPrefix(strs):
	lst = list(zip(*strs))
	prefix = ""
	for val in lst:
		if len(set(val)) == 1:
			prefix += val[0]
		else:
			break
	return prefix

print(longestCommonPrefix(["java","jab","jacob"]))
	
