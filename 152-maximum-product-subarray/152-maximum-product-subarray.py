class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMin, curMax, res = nums[0],nums[0],nums[0]
        for n in nums[1:]:
            candidates = (n, curMin*n, curMax*n)
            curMin = min(candidates)
            curMax = max(candidates)
            res = max(res, curMax)
        
        return res