def twosum(alist, target):
	if len(alist) < 2:
		return False
	
	store_dict = dict()
	stop = False
	index = 0
	while not stop and index < len(alist):
		if alist[index] in store_dict:
			stop = True
			result = [store_dict[alist[index]], index]
		else:
			store_dict[target - alist[index]] = store_dict.get(target - alist[index], index)
			index += 1

	return result

