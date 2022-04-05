class Solution:
    def baseNeg2(self, n: int) -> str:
        if n in [0,1]:
            return str(n)
        if n%2 == 0:
            return self.baseNeg2(n//-2) +'0'
        else:
            return self.baseNeg2((n-1)//-2) + '1'