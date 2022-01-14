# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = deque()
        queue_sum = deque()
        cur = root
        queue.append(cur)
        queue_sum.append(cur.val)
        sum = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                cur = queue.popleft()
                cur_v = queue_sum.popleft()
                if cur.left:
                    queue.append(cur.left)
                    queue_sum.append(cur_v*10+cur.left.val)
                
                if cur.right:
                    queue.append(cur.right)
                    queue_sum.append(cur_v*10+cur.right.val)
                
                if not cur.left and not cur.right:
                    # add the path sum if we reach a leaf node
                    sum += cur_v
        
        return sum