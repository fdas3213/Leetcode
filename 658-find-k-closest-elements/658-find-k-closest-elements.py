class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if k == len(arr):
            return arr
        
        #solution 1. two pointers. O(N) time, O(1) space.
        start, end = 0, len(arr)-1
        while end-start>=k:
            if abs(arr[end]-x)<abs(arr[start]-x):
                start += 1
            else:
                end -=1
        
        return arr[start:end+1]