class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        """
        The idea is that there're only 3 cases:
        1. all k cards are selected from the front
        2. all k cards are selected from the tail
        3. some cards are selected from the front and rest of them are chosen from the tail
        """
        l = len(cardPoints)
        
        if k == l:
            return sum(cardPoints)
        
        frontCumSum = [0 for _ in range(k+1)]
        endCumSum = [0 for _ in range(k+1)]
        
        for i in range(k):
            #compute the cumulative sum from front k cards and from end k cards
            frontCumSum[i+1] = frontCumSum[i] + cardPoints[i]
            endCumSum[i+1] = endCumSum[i] + cardPoints[l-1-i]
            
        maxScore = 0
        
        for i in range(k+1):
            #choose i cards from front, and (k-i) cards from the back
            curSum = frontCumSum[i] + endCumSum[k-i]
            maxScore = max(maxScore, curSum)
        
        return maxScore