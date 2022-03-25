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
        
        closest = root.val
        while root:
            closest = min(root.val, closest, key=lambda x: abs(x-target))
            if target<root.val:
                root = root.left
            else:
                root = root.right
        
        return closest