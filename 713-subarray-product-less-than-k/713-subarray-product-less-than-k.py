class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        start = 0
        ans = 0
        cur = 1
        
        for end in range(len(nums)):
            cur *= nums[end]
            
            while start<=end and cur>=k:
                cur /= nums[start]
                start += 1
            
            ans += max(end-start+1, 0)
        
        return ans