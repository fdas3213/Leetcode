# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        #O(K) to O(N): inorder traversal with a deque. When deque reaches size of k, and distance btw target and new element is larger than dist(first deque element, target), then we can simply stop traversal because future answers will be even further away
        queue = deque([])
        
        def inorder(root):
            if not root:
                return
            
            inorder(root.left)
            if len(queue)==k:
                if abs(root.val-target)<abs(queue[0]-target):
                    queue.popleft()
                else:
                    return
            queue.append(root.val)
            inorder(root.right)
        
        inorder(root)
        
        return [v for v in queue]
            