# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return
        
        def helper(root, curPath, res):
            if not root:
                return
            
            if not root.left and not root.right:
                curPath += str(root.val)
                res.append(curPath)
                return
            
            curPath += str(root.val)
            curPath += "->"
            
            helper(root.left, curPath, res)
            helper(root.right, curPath, res)
            
        res = []
        helper(root, "", res)
        
        return res