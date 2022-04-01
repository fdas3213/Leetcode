class DetectSquares:

    def __init__(self):
        self.points = Counter()

    def add(self, point: List[int]) -> None:
        x,y=point
        self.points[(x,y)] += 1

    def count(self, point: List[int]) -> int:
        x1, y1 = point
        ans = 0
        for (x3,y3), cnt in self.points.items():
            # check if there exists a diagonal point
            if abs(x1-x3)!=abs(y1-y3) or x1-x3==0:
                continue
            # need to check if there exist two points(p1.x, p2.y) and (p2.x,p1.y)
            ans += cnt*self.points[(x1,y3)]*self.points[(x3,y1)]
                
        return ans


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)