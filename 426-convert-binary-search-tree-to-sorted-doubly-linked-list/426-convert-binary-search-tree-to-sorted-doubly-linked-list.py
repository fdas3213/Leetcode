"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        
        stack = []
           
        dummyHead = Node(0, None, None)
        dummy = dummyHead
        
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            
            root = stack.pop()
            dummy.right = root
            root.left = dummy
            dummy = root
            root = root.right
        
        dummy.right = dummyHead.right
        dummyHead.right.left = dummy
        
        return dummyHead.right