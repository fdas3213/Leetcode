/*
Given a linked list, swap every two adjacent nodes and return its head.

Example:

Given 1->2->3->4, you should return the list as 2->1->4->3.
Note:

Your algorithm should use only constant extra space.
You may not modify the values in the list's nodes, only nodes itself may be changed.
 */


public class LC24 {
    public static ListNode swapPairs(ListNode head) {
        if (head == null || head.next == null) return head;
        ListNode out = new ListNode(0);
        out.next = head;
        ListNode copy = out;
        while (copy.next != null && copy.next.next !=null){
            ListNode first = copy.next;
            ListNode sec = copy.next.next;
            first.next = sec.next;
            copy.next = sec;
            copy.next.next = first;
            copy = copy.next.next;
        }
        return out.next;
    }

    public static void main(String[] args){
        ListNode l1 = new ListNode(1,new ListNode(2,new ListNode(3, new ListNode(4))));
        ListNode.toString(swapPairs(l1));
    }
}
