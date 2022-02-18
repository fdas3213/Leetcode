# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow, fast = head, head
        
        for i in range(n):
            fast = fast.next
        #if fast is null, that means n==length of the linkedlist, so we need to remove the head node
        if not fast:
            return slow.next
        
        while fast.next:
            fast = fast.next
            slow = slow.next
        
        #now slow points to the node that needs to be removed
        slow.next = slow.next.next
        
        return head