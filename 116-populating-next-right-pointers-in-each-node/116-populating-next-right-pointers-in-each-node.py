"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        queue = deque()
        queue.append(root)
        cur = root
        while queue:
            size = len(queue)
            pre = None
            for _ in range(size):
                cur = queue.popleft()
                if cur.right:
                    queue.append(cur.right)
                if cur.left:
                    queue.append(cur.left)
                cur.next = pre
                pre = cur
        return root


                    
                    