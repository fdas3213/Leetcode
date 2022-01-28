class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if k == len(arr):
            return arr
        
        #solution 3. Binary search: O(log(n-k)) time and O(1) space
        #set right=len(arr)-k because that's the right most index that left pointer can be
        left, right = 0, len(arr)-k
        while left<right:
            mid = left+(right-left)//2
            #do not use abs here to handle cases where arr[mid]=arr[mid+k], and x is greater than arr[mid+k]. e.g. [1,1,2,2,2,2,2,3,3]
            if x-arr[mid]>arr[mid+k]-x:
                left = mid + 1
            else:
                right = mid
        
        return arr[left:left+k]