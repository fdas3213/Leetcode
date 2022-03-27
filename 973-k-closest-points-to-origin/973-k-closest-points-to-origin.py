class Point:
    def __init__(self, x,y):
        self.x = x
        self.y = y
    
    def dist(self):
        # negative sign turns smaller distance to larger negative values. i.e. 2<5 -> -2>-5
        return -(self.x**2+self.y**2)
    
    def __lt__(self, point):
        return self.dist() < point.dist()
    
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #use a maxheap: O(nlog(k))
        maxHeap = []
        
        for x, y in points[:k]:
            point = Point(x,y)
            heappush(maxHeap, point)
        
        for x,y in points[k:]:
            point = Point(x,y)
            heappushpop(maxHeap, point)
        
        return [[item.x, item.y] for item in maxHeap]