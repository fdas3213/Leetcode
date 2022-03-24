# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        n, m = binaryMatrix.dimensions()
        res = m
        for row in range(n):
            left, right = 0, m-1
            while left<=right:
                mid = left+(right-left)//2
                cur = binaryMatrix.get(row, mid)
                if cur<1:
                    left = mid+1
                else:
                    if cur==1:
                        res = min(res, mid)
                    right = mid - 1
                
                if res == 0:
                    return res
        
        return res if res != m else -1