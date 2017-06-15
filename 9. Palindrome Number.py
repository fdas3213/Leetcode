def ispalindrome(x):
  if (x<0) or (x!=0 and x%10 == 0):
    return False
  else:
    result = 0
    while x != 0:
      result = result * 10 + x%10
      x = x//10
    return x == result
      
