# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0
        
        def helper(root, targetSum, curPath):
            if not root:
                return 0
            
            curPath.append(root.val)
            pathCount, pathSum = 0, 0
            
            for v in curPath[::-1]:
                pathSum += v
                if pathSum == targetSum:
                    pathCount += 1
            
            pathCount += helper(root.left, targetSum, curPath)
            pathCount += helper(root.right, targetSum, curPath)
            
            del curPath[-1]
            
            return pathCount
        
        
        return helper(root, targetSum, [])
        
        
            
            
                