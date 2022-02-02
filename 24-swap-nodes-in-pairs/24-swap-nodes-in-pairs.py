# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        dummy = ListNode(0)
        pre = dummy
        cur = head
        while cur and cur.next:
            n = cur.next
            pre.next = n
            cur.next = n.next
            n.next = cur
            pre = cur
            cur = cur.next
            
        return dummy.next