public class LC21 {

    public static ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        if (l1 == null) return l2;
        if (l2 == null) return l1;

        ListNode newNode = new ListNode(0);
        ListNode n = newNode;
        while (l1 != null && l2 != null){
            if (l1.val < l2.val){
                n.next = l1;
                l1 = l1.next;
            }else{
                n.next = l2;
                l2 = l2.next;
            }
            n = n.next;
        }
        if (l1 != null){
            n.next = l1;
        }
        if (l2 != null){
            n.next = l2;
        }
        return newNode.next;
    }

    public static void main(String[] args){
        ListNode l1 = new ListNode(1, new ListNode(2, new ListNode(4)));
        ListNode l2 = new ListNode(1, new ListNode(3, new ListNode(4)));
        ListNode.toString(l1);
        ListNode.toString(l2);
        ListNode.toString(mergeTwoLists(l1,l2));
    }
}
