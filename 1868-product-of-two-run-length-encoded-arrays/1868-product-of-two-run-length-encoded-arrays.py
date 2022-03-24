class Solution:
    def findRLEArray(self, encoded1: List[List[int]], encoded2: List[List[int]]) -> List[List[int]]:
        p1, p2 = 0,0
        ans = []
        while p1<len(encoded1) and p2<len(encoded2):
            v1, f1 = encoded1[p1][0], encoded1[p1][1]
            v2, f2 = encoded2[p2][0], encoded2[p2][1]
            
            #get the product
            product = v1*v2
            freq = min(f1, f2)
            """
            if one array has a frequncy greater than the min frequency, then 
            we minus it by the min frequency, so that at the next iteration the new
            frequency will be used.
            """
            encoded1[p1][1] -= freq
            encoded2[p2][1] -= freq
            
            # increment only if both frequencies have been used at the current position
            if encoded1[p1][1] == 0:
                p1 += 1
            if encoded2[p2][1] == 0:
                p2 += 1
            
            if not ans or ans[-1][0] != product:
                ans.append([product, freq])
            else:
                ans[-1][1] += freq
        
        return ans