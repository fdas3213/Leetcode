class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        if n<3:
            return res
        
        nums.sort()
        for i in range(n-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            left, right = i+1, n-1
            while left<right:
                cursum = nums[i]+nums[left]+nums[right]
                if cursum<0:
                    left += 1
                elif cursum>0:
                    right -= 1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left<right and nums[left]==nums[left-1]:
                        left += 1
                    while left<right and nums[right]==nums[right+1]:
                        right -= 1
        
        return res