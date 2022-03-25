class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #priority queue: o(nlog(k))
        
        minHeap = []
        for n in nums[:k]:
            heappush(minHeap, n)
        
        for n in nums[k:]:
            heappushpop(minHeap, n)
        
        return minHeap[0]