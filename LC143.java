public class LC143 {
    public static void reorderList(ListNode head) {
        if(head == null || head.next == null) return;
        //first find middle node
        ListNode first = head;
        ListNode sec = head;
        while(sec.next != null && sec.next.next != null){
            first = first.next;
            sec = sec.next.next;
        }
        //reverse second half
        ListNode mid = first;
        ListNode midNext = first.next;
        while(midNext != null){
            ListNode next = midNext.next;
            midNext.next = next.next;
            next.next = mid.next;
            midNext = next;
        }
    }

    public static void main(String[] args){
        ListNode n = new ListNode(0, new ListNode(1, new ListNode(2,
                new ListNode(3, new ListNode(4)))));
        reorderList(n);
    }
}
