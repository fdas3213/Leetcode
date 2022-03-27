class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # use a stack to record the indices of open parenthesis
        stack = []
        # use a list to record non-matching closing parenthesis
        closing_index = []
        # use a variable to check the balance
        
        """
        at the end, we build a new string that ignores indices from 
        stack(which are open parenthesis that have no matching closing parenthesis) 
        and indices from closing_index list
        """
        
        for idx, c in enumerate(s):
            if c not in "()":
                continue
            if c=='(':
                stack.append(idx)
            elif not stack:
                #this means c==')' and balance<=0, which means the current closing parenthesis
                #does not have a matching open parenthesis
                closing_index.append(idx)
            else:
                stack.pop()
        
        ans = ""
        for idx, c in enumerate(s):
            if idx not in stack and idx not in closing_index:
                ans += c

        return ans