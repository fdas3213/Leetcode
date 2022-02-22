class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        n = len(s)
        if n==1:
            return 0
        
        pre, cur, count = 0, 1, 0
        for i in range(1, n):
            if s[i]==s[i-1]:
                cur += 1
            else:
                count += min(pre, cur)
                pre = cur
                cur = 1
        
        return count + min(pre, cur)