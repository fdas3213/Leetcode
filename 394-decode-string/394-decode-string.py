class Solution:
    def decodeString(self, s: str) -> str:
        #use a stack to store digit, and a queue to store letters
        stack = []
        charStack = deque([])
        ans = ""
        #if the number is more than 1 digits, then we need to store previous digits
        prev = 0
        
        for ch in s:
            if ch.isdigit():
                prev = prev*10 + int(ch)
                #stack.append(int(ch))
            elif ch=='[':
                charStack.append(ch)
                stack.append(prev)
                prev = 0
            elif ch.isalpha():
                charStack.append(ch)
            elif ch==']':
                cnt = stack.pop()
                curStr = ""
                while charStack[-1]!='[':
                    char = charStack.pop()
                    curStr = char + curStr
                #now pop the open parenthesis
                charStack.pop()
                
                charStack.append(curStr*cnt)
        
        while charStack:
            ans += charStack.popleft()
        
        return ans
            