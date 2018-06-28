public class insertionsort147 {
    /*public ListNode insertionSortList(ListNode head) {

    }
*/
    public static void main(String[] args){
        ListNode h = new ListNode(10,new ListNode(8, new ListNode(11, new ListNode(14))));
        ListNode n = h.next;
        System.out.println(ListNode.toString(h));
        System.out.println(ListNode.toString(n));
        n.next = new ListNode(9);
        System.out.println(ListNode.toString(h));
        System.out.println(ListNode.toString(n));

        n.val = 100;
        System.out.println(ListNode.toString(h));
        System.out.println(ListNode.toString(n));
    }
}
