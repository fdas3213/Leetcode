class Solution:
    def removeDuplicates(self, s: str) -> str:
        # edge case
        l = len(s)
        if len(s) <= 1:
            return s
        
        stack = []
        for char in s:
            if stack and char==stack[-1]:
                stack.pop()
            else:
                stack.append(char)
                
        return "".join(stack)
        
#         for end in range(1, l):
#             if s[end]==s[end-1]:
#                 newStr = s[:end-1]+s[end+1:]
#                 return self.removeDuplicates(newStr)
                
#         return s
        