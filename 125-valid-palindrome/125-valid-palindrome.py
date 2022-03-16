class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.strip().lower()
        #edge case
        if len(s)<=1:
            return True
        
        left, right = 0, len(s)-1
        while left < right:
            if not s[left].isalpha() and not s[left].isdigit():
                left += 1
            elif not s[right].isalpha() and not s[right].isdigit():
                right -= 1
            elif s[left] != s[right]:
                return False
            else:
                left += 1
                right -= 1
        
        return True