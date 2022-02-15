class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        
        tasks.sort()
        sessions = []
        self.res = len(tasks)
        
        def backtrack(start:int):
            if len(sessions)>self.res:
                #self.res stores the current best solution, so if number of sessions exceeds this best solution, then there's no reason to continue backtracking, hence return
                return
            
            if start==len(tasks):
                #when completed all tasks, store the current solution at result[0]
                self.res = len(sessions)
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
        
        return self.res