# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        res = []
        if not root:
            return res
        
        #inorder traversal
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            
            root = stack.pop()
            if len(res)<k:
                res.append(root.val)
            elif abs(target-root.val)<abs(target-res[0]):
                res.pop(0)
                res.append(root.val)
            elif abs(target-root.val)>=abs(target-res[0]):
                return res
                
            root = root.right
        
        return res