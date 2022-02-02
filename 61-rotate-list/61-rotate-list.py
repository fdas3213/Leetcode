# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k==0:
            return head
        
        # step 1. find the length of the linkedlist
        l = 1
        slow = fast = head
        while fast.next:
            fast = fast.next
            l += 1
        
        k%=l
        
        # step 2. create a circular linkedlist
        fast.next = head
        for i in range(l-k-1):
            slow = slow.next
        
        pre = slow.next
        slow.next = None
        
        return pre
        
        