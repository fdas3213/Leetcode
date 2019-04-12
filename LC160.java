public class LC160 {
    public static ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        if (headA == null || headB == null) return null;
        //find the shorter linkedlist
        int l1 = 0, l2 = 0;
        ListNode copyA = headA;
        ListNode copyB = headB;
        while(copyA != null){
            copyA = copyA.next;
            l1++;
        }
        while(copyB != null){
            copyB = copyB.next;
            l2++;
        }
        //make two linkedlist same length
        if(l1 > l2){
            for (int i =0; i < l1-l2; i++) headA = headA.next;
        }else if (l1 < l2){
            for (int i = 0; i < l2-l1;i++) headB = headB.next;
        }
        while(headA != headB){
            headA = headA.next;
            headB = headB.next;
        }
        return headA;
    }
    public static void main(String[] args){
        ListNode l1 = new ListNode(0, new ListNode(9, new ListNode(1, new ListNode(2, new ListNode(4)))));
        ListNode l2 = new ListNode(3,new ListNode(2, new ListNode(4)));
        ListNode.toString(getIntersectionNode(l1,l2));
    }
}
