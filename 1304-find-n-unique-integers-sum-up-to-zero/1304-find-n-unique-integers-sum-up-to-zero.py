class Solution:
    def sumZero(self, n: int) -> List[int]:
        #if n is even, then choose any n//2 integers from left and right side of 0 respectively. e.g [-3,-2,2,3]
        #if n is odd, choose any n//2 integers from left and right side of 0 respectively, plus a 0. e.g. [-3,2,0,2,3]
        
        res = []
        one_side_count = n//2
        for i in range(1, one_side_count+1):
            res.append(i)
            res.append(-i)
        if n%2 != 0:
            res.append(0)
        
        return res