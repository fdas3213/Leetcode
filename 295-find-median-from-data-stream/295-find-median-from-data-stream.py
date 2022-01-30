class MedianFinder:

    def __init__(self):
        #use max heap to store small elements and min heap to store large elements
        #e.g. minheap = [-2,-1], maxheap = [3,4], and the median would be the mean of the first elements in two heaps
        self.minHeap = []
        self.maxHeap = []
        self.size = 0

    def addNum(self, num: int) -> None:
        if not self.minHeap or -self.minHeap[0]>num:
            heappush(self.minHeap, -num)
        else:
            heappush(self.maxHeap, num)
        
        if len(self.minHeap) > len(self.maxHeap)+1:
            #at the beginning when two items were pushed into the min heap, we need to move one to the maxheap
            heappush(self.maxHeap, -heappop(self.minHeap))
        elif len(self.minHeap) < len(self.maxHeap):
            heappush(self.minHeap, -heappop(self.maxHeap))
                     
        self.size += 1

    def findMedian(self) -> float:
        if self.size%2 ==0:
            return (-self.minHeap[0]+self.maxHeap[0])/2
        else:
            return -self.minHeap[0]
            


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()