class MovingAverage:

    def __init__(self, size: int):
        self.windowSize = size
        # window sum
        self.windowSum = 0
        # maintain a queue of size "size", which records previous "size" number of input
        self.prev = deque()
        
    def next(self, val: int) -> float:
        self.windowSum += val
        self.prev.append(val)
                
        if len(self.prev) > self.windowSize:
            self.windowSum -= self.prev.popleft()
        
        return self.windowSum/len(self.prev)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)