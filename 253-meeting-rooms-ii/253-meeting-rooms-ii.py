class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        """
        Idea: compute number of non-overlapping intervals
        step 1. sort intervals based on start time and end time
        step 2. we add 1 if the current start time is less than the minimum end time, otherwise we increment end time pointer by 1
        
        O(Nlog(N)) for sorting, and O(N) for iterating
        """
        
        startTime = sorted([interval[0] for interval in intervals])
        endTime = sorted([interval[1] for interval in intervals])
        count, end = 0, 0
        for start in startTime:
            if start<endTime[end]:
                count += 1
            else:
                #endTime[end] always points to the earliest endTime, so if new meeting start time is earlier than the
                #earliest endTime, then of course need to add 1 meeting room
                end += 1
        return count