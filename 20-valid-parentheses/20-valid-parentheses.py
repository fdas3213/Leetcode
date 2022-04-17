class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for c in s:
            if c == '(' or c=='[' or c=='{':
                stack.append(c)
            elif not stack:
                # no matching open parenthesis
                return False
            else:
                pre = stack.pop()
                if c==')' and pre!='(':
                    return False
                elif c==']' and pre!='[':
                    return False
                elif c=='}' and pre!='{':
                    return False
        
        return len(stack)==0
                
                