# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        """
        one-pass solution: create a new list while iterating.
        idea: add the head of all linkedlists into the minheap, and 
        add its next node when we pop a head
        """
        minHeap = []
        
        for sublist in lists:
            #step 1. add the head: O(L), L is the number of linkedlists
            if sublist:
                """
                need to add another value as the second value in the tuple because 
                of the TypeError:'<' not supported between instances of ListNode and ListNode.
                By adding id(node), we create a unique identifier for each object/node
                """
                heappush(minHeap, (sublist.val, id(sublist), sublist))
        
        dummy = ListNode(0)
        ans = dummy
        
        while minHeap:
            v, idx, node = heappop(minHeap)
            nxt = node.next
            dummy.next = ListNode(v)
            dummy = dummy.next
            if nxt:
                heappush(minHeap, (nxt.val, id(nxt), nxt))
        
        return ans.next
        
        
        