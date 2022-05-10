# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        Use a hashmap to track the level of the current node and their relative width
        """
        
        levelMap = defaultdict(list)
        
        def dfs(node, level, pos):
            if not node:
                return
            levelMap[level].append(pos)
            
            dfs(node.left, level+1, pos*2)
            dfs(node.right, level+1, pos*2+1)
        
        dfs(root, 1, 1)
        
        ans = -1
        for level in levelMap:
            ans = max(ans, max(levelMap[level])-min(levelMap[level])+1)
        
        return ans
            
            