"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        parent_set = set()
        
        while p:
            parent_set.add(p)
            p = p.parent
        
        while q:
            if q in parent_set:
                return q
            q = q.parent
        
        return None