class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        
        #step 1. iterate from the end to the start of the list and stop when nums[right-1]<nums[right]
        right = len(nums)-1
        while right>0 and nums[right-1]>=nums[right]:
            right -= 1
            
        #step 2. iterate from the end to the start of the list to find the first value that's greater than nums[right-1]
        if right!=0:
            candidate = len(nums)-1
            while candidate>right-1 and nums[candidate]<=nums[right-1]:
                candidate -= 1
            #swap 
            nums[right-1], nums[candidate] = nums[candidate], nums[right-1]
        
        #step 3. sort nums[right:]
        def swap(nums, i, j):
            while i<j:
                nums[i], nums[j] = nums[j],nums[i]
                j -= 1
                i += 1
        
        swap(nums, right, len(nums)-1)