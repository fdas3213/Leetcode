class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        # edge case
        if m==len(nums):
            return max(nums)
        
        def check(arrSum):
            """
            we only need to check if we can split the input into at most m subarrays.
            For example, if arrSum=10, nums=[7,2,5,10,8], then we need to do 4 splits
            to make sure each subarray does not have a subarray sum>10. 
            """
            count, cumSum = 1, 0
            for n in nums:
                cumSum += n
                if cumSum>arrSum:
                    count += 1
                    cumSum = n
            return count<=m
            
        #search space: [max(nums), sum(nums)]
        left, right, minSum = max(nums), sum(nums), sum(nums)
        
        while left<right:
            mid = left+(right-left)//2
            if check(mid):
                #since mid is valid, right should set to mid to be included in 
                #the search space so that we try a value<=mid
                right = mid
                minSum = mid
            else:
                #since mid is not valid, left should be set to mid+1 so that
                #it's not included in the search space
                left=mid+1
        
        return minSum
                
        
        