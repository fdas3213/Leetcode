class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans = len(nums)+1
        
        left, window_sum = 0, 0
        for right, n in enumerate(nums):
            window_sum += n
            while window_sum>=target:
                ans = min(ans, right-left+1)
                window_sum -= nums[left]
                left += 1
        
        return ans if ans!=len(nums)+1 else 0