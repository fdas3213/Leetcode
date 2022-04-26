class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        #check if it's divisible by 2
        if finalSum%2!=0:
            return []
        
        res = []
        
        def backtrack(curSum:int, finalSum:int, n:int, res:List[int]):
            # terminal condition
            if curSum==finalSum:
                return True
            if curSum+n>finalSum:
                return False
            
            for i in range(n, finalSum+1, 2):
                res.append(i)
                if backtrack(curSum+i, finalSum, i+2, res):
                    return True
                res.pop()
            
            return False
        
        if backtrack(0, finalSum, 2, res):
            return res
        
        return []
        