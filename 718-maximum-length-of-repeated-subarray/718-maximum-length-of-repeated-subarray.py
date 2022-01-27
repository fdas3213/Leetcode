class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        l1, l2 = len(nums1), len(nums2)
        dp = [[0 for _ in range(l2+1)] for _ in range(l1+1)]
        
        res = 0
        for i in range(1, l1+1):
            for j in range(1, l2+1):
                if nums1[i-1]==nums2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                    res = max(res, dp[i][j])
        
        return res
        
            