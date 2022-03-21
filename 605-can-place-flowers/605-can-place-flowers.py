class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        #edge case
        if n==0:
            return True
        
        l = len(flowerbed)

        for i in range(l):
            if flowerbed[i]==0:
                left = (i==0) or (flowerbed[i-1]==0)
                right = (i==l-1) or (flowerbed[i+1]==0)
                
                if left and right:
                    n-=1
                    flowerbed[i]=1
            
            if n<=0:
                return True
        
        return False