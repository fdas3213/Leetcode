class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum = nums[0]
        ans = curSum
        
        for n in nums[1:]:
            curSum = max(curSum+n, n) 
            ans = max(ans, curSum)
        
        return ans