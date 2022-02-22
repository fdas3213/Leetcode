# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0 
        self.moves = 0
        
        def dfs(root:TreeNode):
            #the first value records number of subtrees of the current node, and the second value records number of coins of the current node
            if not root:
                return [0,0]
            left = dfs(root.left)
            right = dfs(root.right)
            
            self.moves += abs(left[0]-left[1])+abs(right[0]-right[1])
            return [left[0]+right[0]+1, left[1]+right[1]+root.val]
        
        dfs(root)
        return self.moves