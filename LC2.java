public class LC2 {

    public static ListNode addTwoNumbers(ListNode l1, ListNode l2){
        if (l1 == null) return l2;
        if (l2 == null) return l1;
        if (l1 == null && l2 == null) return null;
        ListNode l = new ListNode(0);
        ListNode out = l;
        int sum = 0;
        while (l1 != null || l2 != null || sum != 0){
            if (l1 != null) {
                sum += l1.val;
                l1 = l1.next;
            }
            if (l2 != null) {
                sum += l2.val;
                l2 = l2.next;
            }
            out.next = new ListNode(sum % 10);
            sum /= 10;
            out = out.next;
        }
        return l.next;
    }

    public static void main(String[] args){
        ListNode n1 = new ListNode(2, new ListNode(4, new ListNode(3)));
        ListNode n2 = new ListNode(5, new ListNode(6, new ListNode(4)));
        System.out.println(ListNode.toString(addTwoNumbers(n1, n2)));
    }
}
