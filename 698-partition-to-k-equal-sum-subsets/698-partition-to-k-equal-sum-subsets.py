class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total%k!=0:
            return False
        subset_sum = total//k
        # use the index of each element to indicate whether an element has been used or not
        used = set()
        
        nums.sort(reverse=True)
        
        def backtrack(start:int, cursum:int, subset_count:int):
            """
            1. cursum == subset sum
            2. collected k subsets
            3. used all elements
            """
            if subset_count==k-1:
                return True
            
            if cursum==subset_sum:
                return backtrack(0, 0, subset_count+1)
            
            #backtrack
            for i in range(start, len(nums)):
                """
                avoid dup: if current element==previous element, and 
                previous element not used, then current element should not be used
                """
                if i>0 and i-1 not in used and nums[i]==nums[i-1]:
                    continue
                
                if i not in used and cursum+nums[i]<=subset_sum:
                    used.add(i)
                    if backtrack(i+1, cursum+nums[i], subset_count):
                        return True
                    used.remove(i)
            
            return False
        
        return backtrack(0, 0, 0)
                