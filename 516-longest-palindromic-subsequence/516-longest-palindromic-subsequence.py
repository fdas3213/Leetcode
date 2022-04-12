class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        l = len(s)
        memo = [[0 for _ in range(l)] for _ in range(l)]
        
        def cntSubseq(l, r, s):
            if l==r:
                return 1
            if l>r:
                return 0
            if memo[l][r]:
                return memo[l][r]
            
            memo[l][r] = 2+cntSubseq(l+1,r-1,s) if s[l]==s[r] else \
                    max(cntSubseq(l+1, r, s), cntSubseq(l, r-1, s))
            
            return memo[l][r]
        
        return cntSubseq(0, l-1, s)