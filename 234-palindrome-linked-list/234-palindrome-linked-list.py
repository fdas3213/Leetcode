# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, head):
        if not head or not head.next:
            return head
        pre = None
        while head:
            n = head.next
            head.next = pre
            pre = head
            head = n
        return pre
        
        
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        #fast, slow pointer, then reverse the slow pointer, and finally compare reversed slow pointer with fast pointer
        if not head or not head.next:
            return True
        
        # step 1. use slow and fast pointer to divide the linkedlist in half
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
        # step 2. reverse slow pointer
        half = self.reverse(slow)
        
        # step 3. compare head with reversed 2nd half
        while half and head:
            if half.val != head.val:
                return False
            half = half.next
            head = head.next
        
        return True