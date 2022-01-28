class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if k == len(arr):
            return arr
        
        #solution 2. maxheap O(N) time, O(k) space.
        maxHeap = []
        for n in arr[:k]:
            heappush(maxHeap, (-abs(n-x), n))
        
        for n in arr[k:]:
            #Heap elements can be tuples. and it will sort by the first element of the tuple
            if -abs(n-x)>maxHeap[0][0]:
                heappushpop(maxHeap, (-abs(n-x), n))
        
        return sorted([tup[1] for tup in maxHeap])