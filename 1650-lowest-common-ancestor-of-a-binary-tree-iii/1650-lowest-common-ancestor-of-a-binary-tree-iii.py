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
        # O(H) solution
        visited = set()

        while p:
            visited.add(p)
            p = p.parent
        
        while q:
            if q in visited:
                #this means q is already on the path of q->root, which is the LCA of p&q
                return q
            q = q.parent
        
        return q