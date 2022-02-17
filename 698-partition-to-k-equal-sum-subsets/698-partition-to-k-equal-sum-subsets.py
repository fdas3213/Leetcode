class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        #check if the array sum can be evenly divided into k parts
        arr_sum = sum(nums)
        if arr_sum%k!=0:
            return False
        
        n = len(nums)
        used = [False for _ in range(n)]
        target_sum = arr_sum//k
        
        nums.sort(reverse=True)
        
        def backtrack(pos:int, count:int, cursum:int):
            #we made k - 1 subsets with target sum and the last subset will also have target sum.
            if count == k-1:
                return True
            
            if cursum==target_sum:
                return backtrack(0, count+1, 0)
                
            for i in range(pos, n):
                # avoid duplicated backtracking
                if i > 0 and not used[i-1] and nums[i] == nums[i-1]:
                    continue
                    
                if not used[i] and cursum+nums[i]<=target_sum:
                    used[i] = True
                    if backtrack(i+1, count, cursum+nums[i]):
                        return True
                    used[i] = False
            
            return False
            
        return backtrack(0, 0, 0)
                
                
            