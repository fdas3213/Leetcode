public class LC206 {
    public static ListNode reverseList(ListNode head) {
        ListNode newhead = null;
        while (head != null){
            ListNode next = head.next;
            head.next = newhead;
            newhead = head;
            head = next;
        }
        return newhead;
    }

    public static void main(String[] args){
        ListNode l = new ListNode(1, new ListNode(2,
                new ListNode(3, new ListNode(4, new ListNode(5)))));
        System.out.println(ListNode.toString(reverseList(l)));
    }
}
