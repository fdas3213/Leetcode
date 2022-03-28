class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        m,n = len(rooms), len(rooms[0])
        dirs = [[0,1],[0,-1],[-1,0],[1,0]]
        queue = deque()
    
        for i in range(m):
            for j in range(n):
                #Push all gates into queue first. Then for each gate update its neighbor cells and push them to the queue.
                if rooms[i][j]==0:
                    queue.append((i,j))
        
        visited = set()
        while queue:
            i, j = queue.popleft()
            for d in dirs:
                x, y = i+d[0], j+d[1]
                if x<0 or y<0 or x>=m or y>=n or rooms[x][y] in [-1,0] or (x,y) in visited:
                    continue
                visited.add((x,y))
                rooms[x][y] = rooms[i][j] + 1
                queue.append((x,y))