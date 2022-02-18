class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        
        closest = sum([nums[i] for i in range(3)])
        mindist = abs(closest-target)
        n = len(nums)
        for i in range(n-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            
            left, right = i+1, n-1
            while left<right:
                cursum = nums[i]+nums[left]+nums[right]
                curdist = abs(cursum-target)
                if curdist<mindist:
                    mindist = curdist
                    closest = cursum
                
                if cursum<target:
                    left+=1
                elif cursum>target:
                    right-=1
                else:
                    return cursum
        
        return closest