def ispalindrome(x):
	if (x<0) or (x!=0 and x%10 == 0):
		return False
	else:
		result = 0
		y = x
		while x > 0:
			result = result * 10 + x%10
			x = x//10
		return y == result

print(ispalindrome(323))
print(ispalindrome(329))
print(ispalindrome(99))
print(ispalindrome(-12))
      
