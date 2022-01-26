class HitCounter:

    def __init__(self):
        self.hit_map = defaultdict(int)
        self.th = 300
    def hit(self, timestamp: int) -> None:
        self.hit_map[timestamp] += 1

    def getHits(self, timestamp: int) -> int:
        valid_time = [k for k in self.hit_map if k>timestamp-self.th and k<=timestamp]
        
        return sum(self.hit_map[k] for k in valid_time)


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)