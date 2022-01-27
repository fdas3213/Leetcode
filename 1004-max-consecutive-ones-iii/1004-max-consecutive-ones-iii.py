class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        start, res = 0, 0
        for end, n in enumerate(nums):
            if n==0:
                k -= 1
                while k<0:
                    if nums[start]==0:
                        k+=1
                    start += 1
            
            res = max(res, end-start+1)
            
        return res