# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.val = 0
        
        def helper(root, treeMap):
            if not root:
                return 0
            
            if root in treeMap:
                return treeMap[root]
            
            left_h = helper(root.left, treeMap)
            right_h = helper(root.right, treeMap)
            
            max_depth = max(left_h, right_h) + 1
            
            treeMap[root] = max_depth
            
            return max_depth
        
        def preorder(root, treeMap):
            if not root:
                return
            max_left = helper(root.left, treeMap)
            max_right = helper(root.right, treeMap)
            self.val = max(self.val, max_left+max_right)
            
            preorder(root.left, treeMap)
            preorder(root.right, treeMap)
        
        preorder(root, {})
        
        return self.val