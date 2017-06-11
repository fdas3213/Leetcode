#using recursion
def rev(num):
	if -10 < num < 10:
		return num
	elif num % 10 == 0:
		return 0
	elif num < -10 and num %10 != 0:
		str_num = str(num)[1:]
		sign = str(num)[0]
		return int(sign + str_num[-1] + str(rev(int(str_num[:-1]))))
	else:
		str_num = str(num)
		return int(str_num[-1] + str(rev(int(str_num[:-1]))))
