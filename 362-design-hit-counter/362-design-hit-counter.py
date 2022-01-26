class HitCounter:

    def __init__(self):
        #Using queue: space and time complexity both O(N)
        self.queue = deque()
        self.th = 300
        self.count = 0
        
    def hit(self, timestamp: int) -> None:
        if self.queue and self.queue[-1][0]==timestamp:
            prev_count = self.queue.pop()[1]
            self.queue.append((timestamp, prev_count+1))
            self.count -= prev_count
        else:
            self.queue.append((timestamp,1))
        self.count += self.queue[-1][1]

    def getHits(self, timestamp: int) -> int:
        while self.queue and timestamp-self.queue[0][0]>=self.th:
            self.count -= self.queue[0][1]
            self.queue.popleft()
        return self.count


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)