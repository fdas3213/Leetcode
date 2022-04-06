class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        if len(nums)<3:
            return 0
        
        nums.sort()
        l = len(nums)
        count = 0
        for i in range(l-1, 1, -1):
            left, right = 0, i-1
            while left<right:
                if nums[i]+nums[left]+nums[right]<target:
                    count += (right-left)
                    left += 1
                else:
                    right -= 1
        
        return count