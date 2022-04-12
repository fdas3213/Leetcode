class Solution:
    def countSubstrings(self, s: str) -> int:
        l = len(s)
        
        def isPalindrome(l:int, r:int, s:str):
            ans = 0
            #expand from the middle to count every possible palindrome substring
            while l>=0 and r<len(s):
                if s[l]!=s[r]:
                    return ans
                l -= 1
                r += 1
                ans += 1
            return ans
        
        cnt = 0
        for i in range(l):
            #middle is every single character
            cnt += isPalindrome(i, i, s)
            #middle is every pair of characters
            cnt += isPalindrome(i, i+1, s)
        
        return cnt