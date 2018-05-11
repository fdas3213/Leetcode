public class removedup83 {
    public static void main(String args[]) {
        ListNode l1 = new ListNode(1, new ListNode(1, new ListNode(2)));
        System.out.println(toString(l1));
        System.out.println(toString(deleteDuplicates(l1)));

        ListNode l2 = new ListNode(1, new ListNode(1, new ListNode(2, new ListNode(3, new ListNode(3)))));
        System.out.println(toString(l2));
        System.out.println(toString(deleteDuplicates(l2)));

        ListNode l3 = new ListNode(1,new ListNode(1, new ListNode(1)));
        System.out.println(toString(l3));
        System.out.println(toString(deleteDuplicates(l3)));

    }

    public static ListNode deleteDuplicates(ListNode head) {
        if (head == null) return head;

        ListNode result = new ListNode(0);
        result.next = head;


        while (head.next != null){
            while (head.val == head.next.val){
                if (head.next.next != null) head.next = head.next.next;
                else {
                    head.next = null;
                    return result.next;
                }
            }
            head = head.next;
        }

        return result.next;
    }

    public static String toString(ListNode l){
        String s = "";
        while (l != null){
            s = s + l.val + " ";
            l = l.next;
        }
        return s;
    }

}
