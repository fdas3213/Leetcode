class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1 for _ in range(len(nums))]
        res = 1
        for i in range(1, len(nums)):
            cur = 1
            for j in range(i):
                if nums[i]>nums[j]:
                    cur = max(cur, dp[j]+1)
            dp[i] = cur
            res = max(res, dp[i])
        return res