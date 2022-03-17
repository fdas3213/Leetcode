class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        mod = 0
        
        l1, l2 = len(num1)-1, len(num2)-1
        #two pointers
        res = ""
        
        while l1>=0 or l2>=0:
            if l1>=0:
                n1 = int(num1[l1])
                mod += n1
                l1 -= 1
            if l2>=0:
                n2 = int(num2[l2])
                mod += n2
                l2 -= 1
            
            res = str(mod%10) + res
            mod = mod // 10
        
        if mod != 0:
            res = str(mod) + res
        
        return res
            