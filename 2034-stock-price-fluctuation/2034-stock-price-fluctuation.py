class StockPrice:

    def __init__(self):
        #hashmap to store timestamp and price
        self.stockPrice = defaultdict(int)
        # use two heaps to update max and min price
        self.maxPrice = []
        self.minPrice = []
        # used to track the current timestamp
        self.maxTimeStamp = 0
        
    def update(self, timestamp: int, price: int) -> None:                   
        self.stockPrice[timestamp] = price
        self.maxTimeStamp = max(self.maxTimeStamp, timestamp)
        
        heappush(self.maxPrice, (-price, timestamp))
        heappush(self.minPrice, (price, timestamp))
        
    def current(self) -> int:
        return self.stockPrice[self.maxTimeStamp]

    def maximum(self) -> int:
        curPrice, timestamp = heappop(self.maxPrice)
        while -curPrice != self.stockPrice[timestamp]:
            # this means the price of the current timestamp has been updated, and we can discard the old price
            curPrice, timestamp = heappop(self.maxPrice)
        
        # add the correct one back to the heap
        heappush(self.maxPrice, (curPrice, timestamp))
        
        return -self.maxPrice[0][0]

    def minimum(self) -> int:
        curPrice, timestamp = heappop(self.minPrice)
        while curPrice != self.stockPrice[timestamp]:
            # this means the price of the current timestamp has been updated, and we can discard the old price
            curPrice, timestamp = heappop(self.minPrice)
        
        # add the correct one back to the heap
        heappush(self.minPrice, (curPrice, timestamp))
        
        return self.minPrice[0][0]


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()