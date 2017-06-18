#This is O(n). 
def longestCommonPrefix(strs):
	prefix = strs[0]

	for val in strs:
		#do not use startswith
		#while not val.startswith(prefix):
		#	prefix = prefix[:-1]
		while val != prefix:
			if len(val) > len(prefix):
				val = val[:len(prefix) -1]
				prefix = prefix[:-1]
			else:
				prefix = prefix[:len(val)-1]
				val = val[:-1]

	return prefix
	
