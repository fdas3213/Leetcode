class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        #need to add 0 here because when cumsum%k==0, and 0 is not in the 
        #hashmap, then it does not return True. Example: [23,2,4,6,6], when
        #cumsum is 35, 35%7==0, so we need 0 in the hashmap
        numMap = {0:-1}
        cumsum = 0
        
        for index, n in enumerate(nums):
            cumsum += n
            #need to log the (mod, index) as the k,v pair so that
            #cumsum is at least composed of two elements
            mod = cumsum%k
            prev = numMap.get(mod, -2)
            if prev!=-2:
                if index-prev>1:
                    return True
            else:
                numMap[mod] = index
            
        return False