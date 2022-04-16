class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        #backtracking
        
        arrSum = sum(nums)
        #cannot be evenly divided
        if arrSum%k!=0:
            return False
        
        l = len(nums)
        used = [False for _ in range(l)]
        nums.sort(reverse=True)
        
        def backtrack(pos:int, curSum:int, cnt:int, subsetSum:int):
            #terminal condition: we now have (k-1) subsets
            if cnt==k-1:
                return True
            
            if curSum==subsetSum:
                return backtrack(0, 0, cnt+1, subsetSum)
            
            for i in range(pos, l):
                #duplicate: if the previous number is not used, then current number should not be used as well
                if i>0 and not used[i-1] and nums[i]==nums[i-1]:
                    continue
                    
                if not used[i] and curSum+nums[i]<=subsetSum:
                    used[i] = True
                    if backtrack(i+1, curSum+nums[i], cnt, subsetSum):
                        return True
                    used[i] = False
            
            return False
        
        return backtrack(0, 0, 0, arrSum//k)
            
            