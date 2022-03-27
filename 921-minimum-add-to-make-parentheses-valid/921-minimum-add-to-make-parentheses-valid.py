class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        ans = 0
        """
        1. use a stack to track number of non-matching open parenthesis
        2. add 1 to answer when we see a non-matching closing parenthesis
        """
        stack = []
        
        for ch in s:
            if ch=='(':
                stack.append(ch)
            elif not stack:
                ans += 1
            else:
                stack.pop()
        
        return ans+len(stack)