class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        """
        Define a search range: [max(weights), sum(weights)].
        To ship weights within "days" days, the capacity should be at least max(weights),
        otherwise there're items that cannot be loaded
        """
        
        def check(capacity):
            count, cumSum = 1, 0
            for weight in weights:
                #if a single weight is greater than capacity, then there's no way
                #to ship this item
                if weight>capacity or count>days:
                    return False
                #when cumSum reaches the maximum load
                if cumSum+weight>capacity:
                    cumSum = 0
                    count += 1
                    
                cumSum += weight
                
            return count<=days
        
        left, right = max(weights), sum(weights)
        while left<right:
            mid = left+(right-left)//2
            if check(mid):
                #when mid capacity is valid, then set right to mid 
                #because right is also an valid answer and should be in the search space
                right = mid
            else:
                #when mid is invalid, then it's not a valid answer, hence setting left=mid+1
                left = mid+1
        
        return right