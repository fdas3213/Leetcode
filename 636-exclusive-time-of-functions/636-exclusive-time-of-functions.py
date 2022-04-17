class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        
        def getLog(log):
            split = log.split(":")
            return int(split[0]), split[1], int(split[2])
        
        res = [0 for _ in range(n)]
        stack = []
        
        for log in logs:
            idx, status, time = getLog(log)
            if status=='start':
                stack.append([idx, status, time])
            else:
                start_idx, start, start_time = stack.pop()
                res[idx] += (time-start_time+1)
                if stack:
                    # if there still exists a running program, then need to subtract the running time by previous 
                    # running program
                    res[stack[-1][0]] -= (time-start_time+1)
        
        return res