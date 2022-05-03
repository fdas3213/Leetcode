# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        #use a hashmap to track row & column information
        #{col: [(row, value)]}
        nodeMap = defaultdict(list)
        self.minLevel = float("inf")
        self.maxLevel = float("-inf")
        
        def dfs(root, col, row):
            if not root:
                return

            self.minLevel = min(col, self.minLevel)
            self.maxLevel = max(col, self.maxLevel)
            nodeMap[col].append((row, root.val))
            dfs(root.left, col-1, row+1)
            dfs(root.right, col+1, row+1)
        
        dfs(root, 0, 0)
        
        ans = []
        
        for level in range(self.minLevel, self.maxLevel+1):
            ans.append([tup[1] for tup in sorted(nodeMap[level], key=lambda x: (x[0], x[1]))])
        
        return ans
        
        
        