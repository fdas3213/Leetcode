#This is O(n). 
def longestCommonPrefix(strs):
	i = 0 
	prefix = strs[0]

	for val in strs:
		while not val.startswith(prefix):
			prefix = prefix[:-1]

	return prefix
	
