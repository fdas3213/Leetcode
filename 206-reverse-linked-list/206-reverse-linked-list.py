# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        pre = ListNode(0)
        pre.next = head
        
        while head.next:
            n = head.next
            head.next = n.next
            n.next = pre.next
            pre.next = n
        
        return pre.next