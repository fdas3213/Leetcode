class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        maxVal = arr[-1]
        #iterate from 1 to maxVal, and decrement k when i is missing from the array
        for i in range(1, maxVal+1):
            if i not in arr:
                k -= 1
            if k==0:
                return i
        
        #if the arr is sorted from [1, maxVal] at an interval of 1, then return maxVal+k
        return maxVal+k