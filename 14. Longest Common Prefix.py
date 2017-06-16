def longestCommonPrefix(strs):
  i = 0 
  stop = False
  s = ""
  
  while not stop and (i < len(strs[0]) or i < len(strs[1])):
    if strs[0][i] == strs[1][i]:
      s += strs[0][i]
    else:
      stop = True
  
  for val in strs[2:]:
    if not val.startswith(s):
      

  return s
