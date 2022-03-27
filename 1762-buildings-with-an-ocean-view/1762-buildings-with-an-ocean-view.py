class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        ans = []
        curMax = heights[-1]
        l = len(heights)
        for index, n in enumerate(heights[::-1]):
            #the last building guarantees to have an ocean view
            if not ans:
                ans.append(l-index-1)
                continue
            if n>curMax:
                ans.append(l-index-1)
                curMax = n
        
        return ans[::-1]