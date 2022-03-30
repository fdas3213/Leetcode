class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # add element to the stack if it is a digit, otherwise pop
        stack = []
        for ch in tokens:
            if ch.isdigit() or ch[1:].isdigit():
                stack.append(int(ch))
            else:
                d1, d2 = stack.pop(), stack.pop()
                if ch=='+':
                    stack.append(d1+d2)
                elif ch=='*':
                    stack.append(d1*d2)
                elif ch=='/':
                    stack.append(int(d2/d1))
                else:
                    stack.append(d2-d1)
        
        ans = 0
        while stack:
            ans += stack.pop()
        
        return ans