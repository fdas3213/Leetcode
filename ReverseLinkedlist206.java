public class ReverseLinkedlist206 {
    public static ListNode reverseList(ListNode head){
        ListNode out = new ListNode(0);
        ListNode s = out.next;
        while (head != null){
            ListNode next = head.next;
            head.next = s;
            s = head;
            head = next;
        }
        return s;
    }
    public static void main(String[] args){
        ListNode l = new ListNode(1, new ListNode(2, new ListNode(3, new ListNode(4))));
        System.out.println(ListNode.toString(l));

        System.out.println(ListNode.toString(reverseList(l)));
    }
}
