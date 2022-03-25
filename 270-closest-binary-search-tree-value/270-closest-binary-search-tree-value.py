# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        if not root or (not root.left and not root.right):
            return root.val
        
        #need to be negative infinity because target could be less than the smallest node value in the tree
        pre = float("-inf")
        stack = []
        
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if target>=pre and target< root.val:
                return pre if abs(pre-target)<abs(root.val-target) else root.val
            pre = root.val
            root = root.right
            
        return pre