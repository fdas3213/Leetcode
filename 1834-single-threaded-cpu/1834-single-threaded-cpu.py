class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # sort by enqueue time
        tasks = [[task[0], task[1], index] for index, task in enumerate(tasks)]
        tasks.sort(key = lambda x: x[0])
        
        #push all tasks whose startTime is less than the curTime to the minHeap
        curTime = tasks[0][0]
        minHeap = []
        
        res = []
        i = 0
        
        while len(res)<len(tasks):
            while i<len(tasks) and tasks[i][0]<=curTime:
                #no need to push startTime because we know they must be less than or equal
                #to the curTime, so just push processing time and index into the minheap
                heappush(minHeap, [tasks[i][1], tasks[i][2]])
                i += 1
            
            if minHeap:
                processing_time, index = heappop(minHeap)
                curTime += processing_time
                res.append(index)
            elif i<len(tasks):
                # reset current time to the task that has the smallest starting time
                curTime = tasks[i][0]
        
        return res