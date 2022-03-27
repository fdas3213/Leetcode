# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        
        nodes = []
        
        def inorder(root):
            # use inorder traversal to get a sorted list of nodes
            if not root:
                return 
            inorder(root.left)
            nodes.append(root)
            inorder(root.right)
        
        def build_tree(low, high):
            if low>high:
                return
            mid = low + (high-low)//2
            root = nodes[mid]
            root.left = build_tree(low, mid-1)
            root.right = build_tree(mid+1, high)
            return root
        
        inorder(root)
        return build_tree(0, len(nodes)-1)