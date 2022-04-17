class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        def partition(left, right, nums):
            i, j = left, right
            #choose a random pivor
            r = random.randint(i, j)
            pivot = nums[r]
            #swap the random number with the first element
            nums[i], nums[r] = nums[r], nums[i]
            
            while i<j:
                while i<len(nums) and nums[i]<=pivot:
                    i += 1
                while j>0 and nums[j]>pivot:
                    j -= 1
                
                #swap
                if i<j:
                    nums[i], nums[j] = nums[j], nums[i]
            
            #swap j with the pivot number
            temp = nums[j]
            nums[j] = pivot
            nums[left] = temp
            
            return j
    
        left, right = 0, len(nums)-1
        k = len(nums)-k
        while left<right:
            pivotIdx = partition(left, right, nums)
            if pivotIdx==k:
                return nums[k]
            elif pivotIdx<k:
                left = pivotIdx+1
            else:
                right = pivotIdx -1
        
        return nums[k]