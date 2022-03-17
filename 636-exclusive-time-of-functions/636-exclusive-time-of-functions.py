class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        
        def get_job_detail(log):
            details = log.split(":")
            return int(details[0]), details[1], int(details[2])
        
        res = [0 for _ in range(n)]
        stack = []
        for log in logs:
            if "start" in log:
                stack.append(log)
            else:
                job, status, time = get_job_detail(stack.pop())
                endjob, endStatus, endTime = get_job_detail(log)
                res[job] += (endTime-time+1)
                if stack:
                    prev_job, prevStatus, prevTime = get_job_detail(stack[-1])
                    res[prev_job] -= (endTime-time+1)
        
        return res
                