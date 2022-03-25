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
        
        queue = deque()
        stack = []
        
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            
            root = stack.pop()
            
            if not queue:
                queue.append(root.val)
            else:
                if abs(target-queue[0])>abs(target-root.val):
                    queue.popleft()
                    queue.append(root.val)
                else:
                    return queue[0]
            
            root = root.right
            
        return queue[0]