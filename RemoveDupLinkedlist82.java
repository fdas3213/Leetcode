public class RemoveDupLinkedlist82 {
    public static ListNode deleteDuplicates(ListNode head) {
        if (head == null || head.next == null) return head;
            ListNode prev = new ListNode(0);
            prev.next = head;
            ListNode cur = prev;
        while (head.next != null){
            ListNode next = cur.next;
            if (head.val == head.next.val) {
                head.next = head.next.next;
                cur.next = head.next;
            }
            else head = head.next;
            if (head.val != next.val) cur = next;
        }
        return prev.next;
    }

    public static void main(String[] args){
        ListNode l = new ListNode(1,new ListNode(1, new ListNode(1, new ListNode(2, new ListNode(3)))));

        System.out.println(ListNode.toString(l));
        System.out.println(ListNode.toString(deleteDuplicates(l)));

        ListNode l1 = new ListNode(1,new ListNode(2, new ListNode(3, new ListNode(3, new ListNode(4,
                new ListNode(4, new ListNode(5)))))));

        System.out.println(ListNode.toString(l1));
        System.out.println(ListNode.toString(deleteDuplicates(l1)));

    }
}
