class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        res = []
        m, n = len(mat), len(mat[0])
        # edge case
        if m==1 and n==1:
            return [1]
        
        # the key here is that diagonal elements have the same row+col value
        max_index = m*n
        diag_sum = defaultdict(deque)
        
        for i in range(m):
            for j in range(n):
                coor_sum = i+j
                if coor_sum%2==0:
                    diag_sum[coor_sum].appendleft(mat[i][j])
                else:
                    diag_sum[coor_sum].append(mat[i][j])
        
        for i in range(max_index):
            res.extend(diag_sum[i])
            
        return res
                
                