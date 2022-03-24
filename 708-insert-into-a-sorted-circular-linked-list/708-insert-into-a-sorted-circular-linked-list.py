"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        if not head:
            node = Node(insertVal)
            node.next = node
            return node
        
        prev, cur = head, head.next
        while prev.next != head:
            # case 1: when insertVal is between the smallest and biggest value
            if insertVal>=prev.val and insertVal<=cur.val:
                break
            # case 2: we're at the tail node. Because the linkedlist is sorted in ascending order,
            # then if prev_v > cur_v, prev is the tail node that has the biggest value.
            elif prev.val>cur.val:
                if insertVal>=prev.val or insertVal<=cur.val:
                    break
            
            prev = cur
            cur = cur.next
        
        # case 3: every node has the same value, so has not inserted the new node yet.
        # in this case, we can insert the new value anywhere. e.g. 3->3->3->3. We can insert 4 at any place
        prev.next = Node(insertVal, cur)
        return head