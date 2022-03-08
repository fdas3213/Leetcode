class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # idea: use a stack to store digits
        stack = []
        
        for token in tokens:
            if token.isdigit() or token.lstrip('-').isdigit():
                stack.append(int(token))
            else:
                e1, e2 = stack.pop(), stack.pop()
                if token=='+':
                    stack.append(e1+e2)
                elif token=='-':
                    stack.append(e2-e1)
                elif token=='*':
                    stack.append(e1*e2)
                else:
                    stack.append(int(e2/e1))
        
        return stack[0]