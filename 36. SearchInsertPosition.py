def searchInsert(nums, target):
	left, right = 0, len(nums) - 1
	stop = False

	if target > nums[len(nums) - 1]:
		return len(nums) 

	if target < nums[0]:
		return 0

	while left <= right:
		mid = (left + right) // 2
		if nums[mid] > target:
			right = mid -1 
			if right >= 0:
				if nums[right] < target:
					return right + 1
			else:
				return 0

		elif nums[mid] < target:
			left = mid + 1
			if left < len(nums):
				if nums[left] > target:
					return left
				else:
					return len(nums)
		else:
			return mid
