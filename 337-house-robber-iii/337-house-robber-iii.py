# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
        
    def rob(self, root: Optional[TreeNode]) -> int:
        
        
        def helper(root, treeMap):
            if not root:
                return 0
            
            if root in treeMap:
                return treeMap[root]

            curMax = root.val

            if root.left:
                curMax += helper(root.left.left, treeMap) + helper(root.left.right, treeMap)
            if root.right:
                curMax += helper(root.right.left, treeMap) + helper(root.right.right, treeMap)

            curMax = max(curMax, helper(root.left, treeMap)+helper(root.right, treeMap))
            treeMap[root] = curMax

            return curMax
        
        return helper(root, {})
            