# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        # level order traversal
        queue = deque([root])
        ans = []
        if not root:
            return ans
        
        while queue:
            size = len(queue)
            curMax = queue[0].val
            
            for i in range(size):
                root = queue.popleft()
                curMax = max(curMax, root.val)
                if root.left:
                    queue.append(root.left)
                if root.right:
                    queue.append(root.right)
            
            ans.append(curMax)
        
        return ans