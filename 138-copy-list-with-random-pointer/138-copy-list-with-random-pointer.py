"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def __init__(self):
        # construct a hashmap
        self.visited = {}
        
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: 
            return head
        
        if head in self.visited:
            return self.visited[head]

        copyNode = Node(head.val)
        self.visited[head] = copyNode
        
        if head.next:
            self.visited[head].next = self.copyRandomList(head.next)
        if head.random:
            self.visited[head].random = self.copyRandomList(head.random)
        
        return self.visited[head]