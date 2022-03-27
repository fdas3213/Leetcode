class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        matMap = defaultdict(deque)
        
        m, n = len(mat), len(mat[0])
        for i in range(m):
            for j in range(n):
                curlevel = i+j
                if curlevel%2!=0:
                    matMap[curlevel].append(mat[i][j])
                else:
                    matMap[curlevel].appendleft(mat[i][j])
        
        ans = []
        for i in range(0, m+n-1):
            ans += list(matMap[i])
        
        return ans
                    