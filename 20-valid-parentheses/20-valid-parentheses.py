class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            if ch=='(' or ch=='[' or ch=='{':
                stack.append(ch)
            elif not stack:
                return False
            elif ch==')' and stack.pop()!='(':
                return False
            elif ch==']' and stack.pop()!='[':
                return False
            elif ch=='}' and stack.pop()!='{':
                return False
            
        return len(stack)==0