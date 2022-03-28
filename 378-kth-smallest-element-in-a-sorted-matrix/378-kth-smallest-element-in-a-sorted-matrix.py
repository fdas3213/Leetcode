class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        #heap
        maxHeap = []
        m,n = len(matrix), len(matrix[0])
        
        for i in range(m):
            for j in range(n):
                if len(maxHeap)<k:
                    heappush(maxHeap, -matrix[i][j])
                else:
                    heappushpop(maxHeap, -matrix[i][j])
        
        return -maxHeap[0]