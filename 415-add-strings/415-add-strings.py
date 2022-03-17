class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        mod = 0
        
        l1, l2 = len(num1)-1, len(num2)-1
        #two pointers
        res = ""
        
        while l1>=0 and l2>=0:
            n1, n2 = int(num1[l1]), int(num2[l2])
            cursum = n1+n2+mod
            res = str(cursum%10) + res
            mod = cursum//10
            l1 -= 1
            l2 -= 1
        
        while l1>=0:
            n1 = int(num1[l1])
            cursum = n1+mod
            res = str(cursum%10) + res
            mod = cursum//10
            l1 -= 1
        
        while l2>=0:
            n2 = int(num2[l2])
            cursum = n2+mod
            res = str(cursum%10) + res
            mod = cursum//10
            l2 -= 1
        
        if mod != 0:
            res = str(mod) + res
        
        return res
            