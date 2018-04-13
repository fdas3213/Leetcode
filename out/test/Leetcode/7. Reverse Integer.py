#using recursion
def reverse(num):
	if num < 0:
		return -reverse(-num)

	result = 0
	while num != 0:
		result = result * 10 + num %10
		num = num // 10
	return result

print(reverse(-123))
