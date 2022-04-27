class DetectSquares:

    def __init__(self):
        #use a hashmap to store {points: count}
        self.points = Counter()

    def add(self, point: List[int]) -> None:
        x, y = point
        self.points[(x,y)] += 1

    def count(self, point: List[int]) -> int:
        #check if there exists a point (x1,y1) s.t. x3-x1==y1-y3
        x3, y3 = point
        ans = 0
        for (x1,y1), cnt in self.points.items():
            if x1!=x3 and abs(x1-x3)==abs(y1-y3):
                p2_cnt = self.points[(x1, y3)]
                p4_cnt = self.points[(x3, y1)]
                ans += cnt*p2_cnt*p4_cnt
        
        return ans
            


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)