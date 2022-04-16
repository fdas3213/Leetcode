class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        l = len(points)
        if l<=2:
            return l
        # at least two points can form a line
        res = 2
        
        def share_slope(p1, p2, p3):
            if (p1[1]-p2[1])*(p1[0]-p3[0])==(p1[0]-p2[0])*(p1[1]-p3[1]):
                return True
            return False
        
        for i in range(l):
            for j in range(i+1, l):
                # set curMax to be the pair of every point
                curMax = 2
                for k in range(l):
                    if k!=i and k!=j:
                        if share_slope(points[i], points[j], points[k]):
                            curMax += 1
                res = max(res, curMax)
        
        return res
                