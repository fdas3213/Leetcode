class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        #sort the input array
        changed.sort()
        res = []
        
        numCnt = Counter(changed)
        
        for n in changed:
            #check freq of current number
            if numCnt[n]==0:
                continue
            #if current number is 0 and frequency is not even
            if n==0 and numCnt[n]%2!=0:
                return res
            #need to decrement both n and n*2
            double = n*2
            if double not in numCnt or numCnt[double]<=0:
                return []
            
            numCnt[n] -= 1
            numCnt[double] -= 1
            res.append(n)
        
        return res