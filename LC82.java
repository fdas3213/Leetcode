public class LC82 {
    public static ListNode deleteDuplicates(ListNode head){
        if (head == null || head.next == null) return head;
        ListNode newhead = new ListNode(0);
        newhead.next = head;
        ListNode pre = newhead;
        ListNode cur = newhead.next;
        while(cur!=null){
            while(cur.next != null && cur.val == cur.next.val){
                cur = cur.next;
            }
            if (pre.next == cur) pre= pre.next;
            else {
                pre.next = cur.next;
            }
            cur = cur.next;
        }
        return newhead.next;
    }
    public static void main(String[] args){
        ListNode t1 = new ListNode(1,new ListNode(1,new ListNode(1,new ListNode(2,
                new ListNode(3)))));
        ListNode t2 = new ListNode(1,new ListNode(2, new ListNode(3,
                new ListNode(3, new ListNode(4,new ListNode(4, new ListNode(5)))))));
        System.out.println(ListNode.toString(deleteDuplicates(t1)));
        System.out.println(ListNode.toString(deleteDuplicates(t2)));
    }
}
