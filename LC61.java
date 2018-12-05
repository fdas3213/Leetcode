public class LC61 {
    private static ListNode rotateRight(ListNode head, int k) {
        if (head == null || head.next == null) return head;
        ListNode copy = head;
        int length = 1, start = 0;
        while (head.next != null){
            length++;
            head = head.next;
        }
        if(k == length || k%length == 0) return copy;
        ListNode dup = new ListNode(0);
        ListNode first = dup;
        while(start != length - k%length){
            first.next = new ListNode(copy.val);
            first = first.next;
            copy = copy.next;
            start++;
        }
        ListNode output = copy;
        while(output.next != null) output = output.next;
        output.next = dup.next;
        return copy;
    }

    public static void main(String[] args){
        ListNode t = new ListNode(0, new ListNode(1, new ListNode(2)));
        System.out.println(ListNode.toString(rotateRight(t, 4)));
        ListNode t1 = new ListNode(1, new ListNode(2, new ListNode(3, new ListNode(4, new ListNode(5)))));
        System.out.println(ListNode.toString(rotateRight(t1,2)));
        ListNode t2 = new ListNode(1,new ListNode(2));
        System.out.println(ListNode.toString(rotateRight(t2,5)));

    }
}
