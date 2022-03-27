# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        nodeMap = defaultdict(list)
        self.curMin, self.curMax = 0,0
        if not root:
            return ans
        
        def dfs(root, row, level):
            if not root:
                return
            
            nodeMap[level].append((row, root.val))
            self.curMin = min(self.curMin, level)
            self.curMax = max(self.curMax, level)
                        
            dfs(root.left, row+1, level-1)
            dfs(root.right, row+1, level+1)
        
        dfs(root, 0, 0)
        
        for i in range(self.curMin, self.curMax+1):
            # sort based on row number
            cur = sorted(nodeMap[i], key=lambda x: (x[0], x[1]))
            ans.append([tup[1] for tup in cur])
        
        return ans
            