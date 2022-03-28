class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        if k==len(nums):
            return len(nums)
        
        start, ans = 0, 0
        for end, n in enumerate(nums):
            if n==0:
                # decrement k when n is 0
                k -= 1
                # shrink the window when k<0
                while k<0:
                    if nums[start]==0:
                        k += 1
                    start += 1
                        
            ans = max(ans, end-start+1)
        
        return ans