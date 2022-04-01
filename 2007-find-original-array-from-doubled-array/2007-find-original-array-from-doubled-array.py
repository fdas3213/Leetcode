class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        res = []
        
        counts = Counter(changed)
        changed.sort()
        l = len(changed)
        
        for i, n in enumerate(changed):
            # skip numbers whose count is 0 because they've already been a double of other numbers
            if counts[n]==0:
                continue
            doubled = n*2
            if n==0:
                if counts[n]%2 !=0:
                    return []
                counts[n]-=2
                res.append(n)
                continue
            
            if doubled not in counts or counts[doubled]==0:
                return []
            
            # decrement the count of both the current number and its double 
            counts[n]-=1
            counts[doubled]-=1
            res.append(n)
        
        return res