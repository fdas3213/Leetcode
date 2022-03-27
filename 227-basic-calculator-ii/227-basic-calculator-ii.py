class Solution:
    def calculate(self, s: str) -> int:
        #idea: if char is a digit, add to stack, otherwise pop from the stack and add the value back
        stack = []
        prev_operator = '+'
        #track numbers with more than one digit
        n = 0
        s=s.strip()
        for i, ch in enumerate(s):    
            if ch==' ':
                continue
            
            if ch.isdigit():
                n = n*10+int(ch)
            
            if not ch.isdigit() or i==len(s)-1:
                if prev_operator=='+':
                    stack.append(n)
                elif prev_operator=='*':
                    prev = stack.pop()
                    stack.append(n*prev)
                elif prev_operator=='/':
                    prev = stack.pop()
                    stack.append(int(prev/n))
                elif prev_operator=='-':
                    stack.append(-n)
                prev_operator = ch
                n = 0
                
        ans = 0
        while stack:
            ans += stack.pop()
        return ans