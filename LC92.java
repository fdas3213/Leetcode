public class LC92 {
    public static ListNode reverseBetween(ListNode head, int m, int n){
        /*
        1->2->3->4->5, m = 2, n=4
        1->4->3->2->5
         */
        if (head == null) return null;
        ListNode out = new ListNode(0);
        out.next = head;
        ListNode pre = out;
        for (int i = 1; i <m; i++) pre= pre.next;
        ListNode start = pre.next;
        ListNode then = start.next;
        for (int i =0; i <n-m;i++){
            start.next = then.next;
            then.next = pre.next;
            pre.next = then;
            start = start.next;
        }
        return out;

    }
}
