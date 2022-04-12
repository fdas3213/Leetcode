class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        l = len(s)
        
        dp = [[0 for _ in range(l)] for _ in range(l)]
        
        # i is the left pointer
        for i in range(l-1,-1,-1):
            #a single character itself is a palindrome
            dp[i][i] = 1
            # j is the right pointer
            for j in range(i+1, l, 1):
                if s[i]==s[j]:
                    dp[i][j] = dp[i+1][j-1]+2
                else:
                    #current index is the max of left and bottom
                    dp[i][j] = max(dp[i][j-1], dp[i+1][j])
        
        #dp[0][l-1] stores the longest subsequence of the entire string
        return dp[0][l-1]
        