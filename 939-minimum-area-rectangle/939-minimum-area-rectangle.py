class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        #two points (x1,y1), (x3,y1), then we need to find (x1,y3) and (x3,y1)
        area = float('inf')
        #need to use a hashmap {x: a set of y's}
        
        pointsMap = defaultdict(set)
        for point in points:
            pointsMap[point[0]].add(point[1])
            
        l = len(points)
        for i, p1 in enumerate(points):
            p1 = points[i]
            for j in range(i+1, l):
                p3 = points[j]
                # if two points share the same x/y coordinates, they cannot be diagonal
                if p1[0]==p3[0] or p1[1]==p3[1]:
                    continue
                    
                curArea = abs(p3[1]-p1[1])*abs(p3[0]-p1[0])
                
                if curArea<area and p3[1] in pointsMap[p1[0]] and p1[1] in pointsMap[p3[0]]:
                    area = curArea
        
        return area if area!=float("inf") else 0