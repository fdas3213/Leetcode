class Solution:
    def validPalindrome(self, s: str) -> bool:
        # edge case
        if len(s) <= 1:
            return True
        
        def isValid(s, left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True
        
        left, right = 0, len(s)-1
        
        while left<right:
            if s[left] != s[right]:
                return isValid(s, left+1, right) or isValid(s, left, right-1)
            else:
                left += 1
                right -= 1
        
        return True