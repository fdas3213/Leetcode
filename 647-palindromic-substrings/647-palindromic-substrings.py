class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0
        
        def countPalindrome(s:str, left:int, right:int) -> int:
            ans = 0
            while left>=0 and right<len(s):
                if s[left]!=s[right]:
                    return ans
                left -= 1
                right += 1
                ans += 1
            
            return ans
        
        for i in range(len(s)):
            # center for odd-length palindrome
            ans += countPalindrome(s, i, i)
            # center for even-length palindrome
            ans += countPalindrome(s, i, i+1)
        
        return ans