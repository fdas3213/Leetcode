class StockPrice:

    def __init__(self):
        self.timePrice = defaultdict(int)
        self.time = 0
        self.maxPrice = []
        self.minPrice = []

    def update(self, timestamp: int, price: int) -> None:
        self.timePrice[timestamp] = price
        self.time = max(self.time, timestamp)
        
        heappush(self.maxPrice, (-price, timestamp))
        heappush(self.minPrice, (price, timestamp))
        
    def current(self) -> int:
        return self.timePrice[self.time]

    def maximum(self) -> int:
        price, time = heappop(self.maxPrice)
        while -price != self.timePrice[time]:
            price, time = heappop(self.maxPrice)
        #need to push the last element back into the heap
        heappush(self.maxPrice,(price, time))
        
        return -self.maxPrice[0][0]

    def minimum(self) -> int:
        price, time = heappop(self.minPrice)
        while price != self.timePrice[time]:
            price, time = heappop(self.minPrice)
        #need to push the last element back into the heap
        heappush(self.minPrice,(price, time))
        
        return self.minPrice[0][0]


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()