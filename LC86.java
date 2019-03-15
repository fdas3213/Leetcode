public class LC86 {
    private static ListNode partition(ListNode head, int x){
        ListNode dummy1 = new ListNode(0), dummy2 = new ListNode(0);
        ListNode cur1 = dummy1, cur2 = dummy2;
        while(head != null){
            if(head.val < x){
                cur1.next = head;
                cur1 = cur1.next;
            }else{
                cur2.next = head;
                cur2 = cur2.next;
            }
            head = head.next;
        }
        cur2.next = null;
        cur1.next = dummy2.next;
        return dummy1.next;
    }


    public static void main(String[] args){
        ListNode t1 = new ListNode(1, new ListNode(4, new ListNode(3,
                new ListNode(2, new ListNode(5, new ListNode(2))))));
        ListNode.toString(partition(t1,3));
    }
}
