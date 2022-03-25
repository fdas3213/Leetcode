class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        def partition(left, right):
            i, j = left, right
            # randomly choose a pivot for optimization
            r = random.randint(left, right)
            pivot = nums[r]
            # swap pivot with the first element
            nums[i], nums[r] = nums[r], nums[i]
            
            while i<j:
                #place all elements less than pivot to the left of pivot
                while i<right and nums[i]<=pivot:
                    i += 1
                #place all elements greater than pivot to the right of pivot
                while j>0 and nums[j]>pivot:
                    j -= 1
                
                if i<j:
                    nums[i], nums[j] = nums[j], nums[i]
            
            #swap with pivot
            nums[j], nums[left] = nums[left], nums[j]
            return j
        
        left, right = 0, len(nums)-1
        #kth largest element is the same as N - kth smallest element. 
        #[1,2,3,4,5], 2nd largest element is the 3rd smallest element
        k = len(nums)-k
        while left<right:
            pivotIndex = partition(left, right)
            if pivotIndex==k:
                return nums[k]
            elif pivotIndex>k:
                right = pivotIndex-1
            else:
                left = pivotIndex+1
        
        return nums[k]