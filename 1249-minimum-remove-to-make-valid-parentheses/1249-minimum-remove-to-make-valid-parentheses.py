class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        """
        1. balance should not be negative at any point
        2. balance should be 0 in the end
        """
        # use a stack to store the indices of open parenthesis that do not have a matching closing parenthesis
        stack = []
        # use another list to store the indices of closing parenthesis that do not have a matching open parenthesis
        closing = []
        
        for index, ch in enumerate(s):
            if ch!='(' and ch!=')':
                continue
                
            if ch=='(':
                stack.append(index)
            elif not stack:
                # no matching open parenthesis
                closing.append(index)
            else:
                stack.pop()
        
        ans = ""
        for index, ch in enumerate(s):
            if index not in stack and index not in closing:
                ans += ch
        
        return ans