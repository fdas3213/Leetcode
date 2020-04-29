public class LC143 {
    public static void reorderList(ListNode head) {
        if(head == null || head.next == null) return;
        ListNode fast = head, slow = head;
        // find middle of list
        while(fast.next != null && fast.next.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }
        ListNode newhead = slow.next;
        slow.next = null;
        //reverse the 2nd half
        newhead = reverse(newhead);
        //merge first and second half
        merge(head, newhead);
    }

    private static ListNode reverse(ListNode head){
        ListNode prev = null, cur = head;
        while(cur != null){
            ListNode next = cur.next;
            cur.next = prev;
            prev = cur;
            cur = next;
        }
        return prev;
    }

    private static void merge(ListNode l1, ListNode l2){
        while(l2 != null){
            ListNode next = l2.next;
            l2.next = l1.next;
            l1.next = l2;
            l1 = l2.next;
            l2 = next;
        }
    }

    public static void main(String[] args){
        ListNode n1 = new ListNode(1, new ListNode(2, new ListNode(3, new ListNode(4))));
        ListNode n2 = new ListNode(1, new ListNode(2, new ListNode(3, new ListNode(4, new ListNode(5)))));
        reorderList(n1);
        ListNode.toString(n1);
        //reorderList(n2);
    }
}
