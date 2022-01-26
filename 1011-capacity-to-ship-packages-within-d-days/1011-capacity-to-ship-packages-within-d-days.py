class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def canShip(weight):
            #check if we ship at most "weight" everyday, can we complete within "days" days
            total = 0
            d = 1
            for w in weights:
                total += w
                if total > weight:
                    d += 1
                    total = w
                if d > days:
                    return False
            
            return True
        
        #The mininum we should ship on any day is the max weight b.c. otherwise we cannot complete this task. 
        #The maximum we can ship on any day is the sum of all weights
        left, right = max(weights), sum(weights)
        while left < right:
            mid = left+(right-left)//2
            if not canShip(mid):
                #if we cannot complete shipping within "days" days, then we need to increase the shipping weight, so we move left pointer 
                left = mid + 1
            else:
                #if we can complete shipping within "days" days, then the maximum boundary is mid because it guarantees a solution, which may or may not be the optimal one, so right needs to be inclusive of mid
                right = mid
        
        return left