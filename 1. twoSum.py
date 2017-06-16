#Temporarily a O(n^2) solution
def twoSum(num, target):
	index = 0
	found = False
	while index < len(num) and not found:
		index2 = index + 1

		while index2 < len(num) and not found:
			result = num[index] + num[index2]
			if result == target:
				found = False
				lst = [index,index2]
			index2 += 1
		index += 1
	return lst
