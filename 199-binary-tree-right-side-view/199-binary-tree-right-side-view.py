# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #bfs
        if not root:
            return []
        res = []
        queue = deque()
        queue.append(root)
        while queue:
            size = len(queue)
            for _ in range(size):
                root = queue.popleft()
                if _ == 0:
                    res.append(root.val)
                if root.right:
                    queue.append(root.right)
                if root.left:
                    queue.append(root.left)
        return res