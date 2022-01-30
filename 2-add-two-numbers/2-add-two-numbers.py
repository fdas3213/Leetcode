# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        pre = ListNode(0)
        ans = pre
        cursum = 0
        while l1 or l2:
            if l1:
                cursum += l1.val
                l1 = l1.next
            if l2:
                cursum += l2.val
                l2 = l2.next
            
            pre.next = ListNode(cursum%10)
            pre = pre.next
            cursum //= 10
    
        if cursum != 0:
            pre.next = ListNode(cursum)
            pre = pre.next
        
        return ans.next