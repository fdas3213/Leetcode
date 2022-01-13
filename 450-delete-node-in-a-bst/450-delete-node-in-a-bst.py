# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def successor(self, root):
        root = root.right
        while root.left:
            root = root.left
        return root.val

        
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # case 1. key is on the leaf node
            if not root.left and not root.right:
                root = None
            # case 2. no left child
            elif root.right and not root.left:
                return root.right
            # case 3. no right child
            elif root.left and not root.right:
                return root.left
            # case 4. has both left and right -> need to find its successor
            else:
                root.val = self.successor(root)
                root.right = self.deleteNode(root.right, root.val)
                
        
        return root

        
        
            