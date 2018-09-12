

public class LC203 {
    public static ListNode removeElements(ListNode head, int val) {
        ListNode out = new ListNode(0);
        out.next = head;
        ListNode copy = out;
        while (copy.next != null){
            if (copy.next.val == val){
                ListNode n = copy.next;
                copy.next = n.next;
            }else {
                copy = copy.next;
            }
        }
        return out.next;
    }

    public static void main(String[] args){
        ListNode n1 = new ListNode(1,new ListNode(2,new ListNode(6,new ListNode(3, new ListNode(4,
                new ListNode(5, new ListNode(6)))))));
        System.out.println(ListNode.toString(removeElements(n1, 6)));
    }
}
