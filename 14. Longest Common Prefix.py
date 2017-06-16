#This is O(n^2). 
def longestCommonPrefix(strs):
	i = 0 
	stop = False
	s = ""
  
	while not stop and (i < len(strs[0]) or i < len(strs[1])):
		if strs[0][i] == strs[1][i]:
			s += strs[0][i]
		else:
			stop = True
		i +=1
	

	index = 0

	for val in strs[2:]:
		while not val.startswith(s):
			s = s[:-1]

	return s
