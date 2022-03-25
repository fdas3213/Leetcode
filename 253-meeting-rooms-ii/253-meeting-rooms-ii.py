class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:        
        minHeap = []
        intervals = sorted(intervals, key=lambda x:x[0])
        for interval in intervals:
            if not minHeap:
                heappush(minHeap, (interval[1], interval[0]))
                continue
            
            if interval[0]<minHeap[0][0]:
                heappush(minHeap, (interval[1], interval[0]))
            else:
                heappushpop(minHeap, (interval[1], interval[0]))
        
        return len(minHeap)