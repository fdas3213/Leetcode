class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        l1, l2, n = -1, -1, len(wordsDict)
        min_dist = n
        for index, word in enumerate(wordsDict):
            if word==word1:
                l1 = index
            elif word==word2:
                l2 = index
            
            if l1!=-1 and l2!=-1:
                min_dist = min(min_dist, abs(l1-l2))
            
            if min_dist == 1:
                #the minimum distance is 1, so if we reach this distance, we directly return
                return min_dist
        
        return min_dist