public class LC83 {
    public static ListNode deleteDuplicates(ListNode head) {
        if (head == null) return head;
        ListNode out = new ListNode(0);
        out.next = head;

        while(head.next != null){
            if (head.val == head.next.val) head.next = head.next.next;
            else head = head.next;
        }
        return out.next;
    }
    public static void main(String[] args){
        ListNode t1 = new ListNode(1,new ListNode(2,new ListNode(2,new ListNode(3,new ListNode(3)))));
        ListNode.toString(deleteDuplicates(t1));
        ListNode t2 = new ListNode(1,new ListNode(1));
        ListNode.toString(deleteDuplicates(t2));
        ListNode t3 = new ListNode(1,new ListNode(1, new ListNode(1)));
        ListNode.toString(deleteDuplicates(t3));
    }
}
