class Solution:
    def longestPalindrome(self, s: str) -> str:     
        l = len(s)
        dp = [[0]*l for _ in range(l)]
        ans = ""
        for i in range(l-1, -1, -1):
            dp[i][i] = True
            if len(ans)<1:
                ans = s[i]
            for j in range(i+1, l, 1):
                # check if s[i] and s[j] matches, if it matches, and the inner substring s[i+1:j-1]
                # is a palindrome, then s[i:j+1] is also a palindrome
                if s[i]==s[j] and (j-i<3 or dp[i+1][j-1]):
                    dp[i][j] = True
                
                if dp[i][j] and len(ans)<j-i+1:
                    ans = s[i:j+1]
                
        return ans