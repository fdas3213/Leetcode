public class LC148 {
    public static ListNode sortList(ListNode head){
        if(head == null || head.next == null) return head;
        //cut linkedlist to 2 halves
        ListNode prev = null, slow = head, fast = head;
        while(fast != null && fast.next != null){
            prev = slow;
            slow = slow.next;
            fast = fast.next.next;
        }
        prev.next = null;
        //sort two halves recursively
        ListNode first = sortList(head);
        ListNode second = sortList(slow);
        //merge two lists
        return merge(first, second);
    }

    private static ListNode merge(ListNode l1, ListNode l2){
        if(l1 == null) return l2;
        if(l2 == null) return l1;
        ListNode out = new ListNode(0);
        ListNode copy = out;
        while(l1 != null && l2 != null){
            if(l1.val <= l2.val) {
                out.next = new ListNode(l1.val);
                l1 = l1.next;
            } else {
                out.next = new ListNode(l2.val);
                l2 = l2.next;
            }
            out = out.next;
        }
        if (l1 != null) out.next = l1;
        if (l2 != null) out.next = l2;
        return copy.next;
    }

    public static void main(String[] args){
        ListNode l = new ListNode(2, new ListNode(-1, new ListNode(3,
                new ListNode(0, new ListNode(4)))));
        ListNode.toString(sortList(l));
    }
}
