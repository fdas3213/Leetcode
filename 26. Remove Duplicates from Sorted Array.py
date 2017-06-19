def removeDuplicates(num):
  for i in range(len(num[1:])):
    if num[i-1] == num[i]:
      num.remove(num[i])
  
  return len(num)
