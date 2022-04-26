class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        #check if it's divisible by 2
        if finalSum%2!=0:
            return []
        
        ans = []
        even = 2
        cur = 0
        #iteratively add even integers
        while cur+even <= finalSum:
            ans.append(even)
            cur += even
            
            even += 2
        
        difference = finalSum-cur
        ans[-1] += difference
        
        return ans
            