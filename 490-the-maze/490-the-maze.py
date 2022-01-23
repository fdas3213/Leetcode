class Solution:
    
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        
        self.dirs = [[1,0],[-1,0],[0,1],[0,-1]]
    
        def dfs(i, j, visited):
            m, n = len(maze), len(maze[0])
            
            if (i,j) in visited:
                return False
            
            visited.add((i,j))
            
            if [i,j] == destination:
                return True
            
            for d in self.dirs:
                x = i + d[0]
                y = j + d[1]
                
                while x>=0 and y>=0 and x<m and y< n and maze[x][y]==0:
                    x += d[0]
                    y += d[1]
                    
                #Because we overshoot by an extra cell due to while loop becoming invalid, so we reduce it be 1 to make the cell valid again.
                
                x -= d[0]
                y -= d[1]
                
                if dfs(x, y, visited):
                    return True
            
            return False   
        
        s_i, s_j = start[0], start[1]
        
        return dfs(s_i, s_j, set())