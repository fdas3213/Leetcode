class MovingAverage:

    def __init__(self, size: int):
        self.windowSize = size
        # window sum
        self.windowSum = 0
        self.count = 0
        # maintain a queue of size 3, which records previous three input
        self.prev = deque()
        
    def next(self, val: int) -> float:
        self.windowSum += val
        self.prev.append(val)
        self.count += 1
        
        if self.count > self.windowSize:
            self.windowSum -= self.prev.popleft()
        
        return self.windowSum/self.count if self.count<self.windowSize else self.windowSum/self.windowSize


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)