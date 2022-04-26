class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #stack
        
        stack = []
        
        for token in tokens:
            if token.isdigit() or token[1:].isdigit():
                stack.append(int(token))
            else:
                n1 = stack.pop()
                n2 = stack.pop()
                if token=='+':
                    stack.append(n1+n2)
                elif token=='*':
                    stack.append(n1*n2)
                elif token=='-':
                    stack.append(n2-n1)
                elif token=='/':
                    stack.append(int(n2/n1))
        
        ans = 0
        while stack:
            ans += stack.pop()
        
        return ans