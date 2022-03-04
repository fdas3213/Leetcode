class Solution:
    def checkValidString(self, s: str) -> bool:
        ast_stack = []
        p_stack = [] 
        
        for i, ch in enumerate(s):
            if ch == '(':
                p_stack.append(i)
            elif ch == ')':
                if not p_stack and not ast_stack:
                    return False
                elif p_stack:
                    p_stack.pop()
                else:
                    ast_stack.pop()
            else:
                ast_stack.append(i)
        
        while p_stack and ast_stack:
            #left parenthesis cannot be after an asterisk
            if (p_stack.pop() > ast_stack.pop()):
                return False
        
        #by the end p_stack should not have any open left parenthesis
        return len(p_stack)==0
            
                