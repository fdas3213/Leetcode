class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        #essentially this problem is asking for numbers in the array, can we find their double-valued number. The tricky part is some numbers are negative, so after sorting, -4 occurs before -2. Therefore if the current number is negative, we either divide or multiply 2. 
        counts = Counter(arr)
        arr.sort()
        
        for n in arr:
            if counts[n]==0:
                continue
            double = n*2 if n>=0 else n/2
            #when n is 0 and there're not even number of '0's to match
            if n==0 and counts[n]%2!=0:
                return False
            
            if double not in counts or counts[double]==0:
                return False
            
            # decrement the count of current number and doubled number
            counts[n]-=1
            counts[double]-=1
        
        return True