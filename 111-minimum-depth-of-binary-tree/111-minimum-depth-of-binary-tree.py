# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        #level order traversal
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        
        queue = deque()
        queue.append(root)
        depth = 1
        while queue:
            size = len(queue)
            
            for _ in range(size):
                root = queue.popleft()
                if not root.left and not root.right:
                    return depth
                if root.left:
                    queue.append(root.left)
                if root.right:
                    queue.append(root.right)
            depth += 1
        
        return depth
            