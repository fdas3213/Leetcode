#using recursion
def rev(num):
	if -10 < num < 10:
		return num
	elif num % 10 == 0:
		return 0
	else:
		str_num = str(num)
		return int(str_num[-1] + str(rev(int(str_num[:-1]))))

print(rev(10))
print(rev(7))
print(rev(123))
print(rev(456))