class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        
        tasks.sort()
        sessions = []
        result = [len(tasks)]
        
        def backtrack(start:int):
            if len(sessions)>result[0]:
                #at most n sessions
                return
            
            if start==len(tasks):
                result[0] = len(sessions)
                return
            
            for i in range(len(sessions)):
                if sessions[i]+tasks[start]<=sessionTime:
                    sessions[i] += tasks[start]
                    backtrack(start+1)
                    sessions[i] -= tasks[start]
            
            sessions.append(tasks[start])
            backtrack(start+1)
            sessions.pop()
            
        backtrack(0)
        
        return result[0]