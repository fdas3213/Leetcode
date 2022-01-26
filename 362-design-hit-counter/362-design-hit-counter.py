class HitCounter:

    def __init__(self):
        self.queue = deque()
        self.th = 300
    def hit(self, timestamp: int) -> None:
        self.queue.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        while self.queue and timestamp-self.queue[0]>=self.th:
            self.queue.popleft()
        return len(self.queue)


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)