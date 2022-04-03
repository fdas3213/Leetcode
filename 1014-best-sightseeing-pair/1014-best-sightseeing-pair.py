class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        n = len(values)
        
        maxEndGain = values[n-1]-(n-1)
        maxGain = 0
        
        for i in range(n-2,-1,-1):
            #maxEndGain[i] = max(maxEndGain[i+1], endGain[i+1])
            maxEndGain = max(maxEndGain, values[i+1]-(i+1))
            maxGain = max(maxGain, values[i]+i+maxEndGain)
        
        return maxGain