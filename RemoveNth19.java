import java.util.List;

public class RemoveNth19 {
    public static ListNode removeNthFromEnd(ListNode head, int n){
        if (head == null) return head;
        ListNode prev = new ListNode(0);
        prev.next = head;
        ListNode cur = prev.next;
        int num = 0;
        while (head.next != null){
            head = head.next;
            num ++;
        }
        int start = 0;
        if (start > num -n){
            prev.next = cur.next;
            return prev.next;
        }

        while (start < num - n){
            cur = cur.next;
            start ++;
        }
        cur.next = cur.next.next;
        return prev.next;
    }

    public static void main(String[] args){
        ListNode l = new ListNode(1, new ListNode(2, new ListNode(3, new ListNode(4, new ListNode(5)))));
        ListNode.toString(l);

        ListNode.toString(removeNthFromEnd(l,2));

        ListNode l1 = new ListNode(1, new ListNode(2));
        ListNode.toString(removeNthFromEnd(l1,1));

        ListNode l2 = new ListNode(1);
        ListNode.toString(removeNthFromEnd(l2,1));
    }
}
