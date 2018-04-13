import java.util.List;

public class ListNode {
    int val;
    ListNode next;

    ListNode(int x){
        this.val = x;
    }
    ListNode(int x, ListNode n){
        this.val = x;
        this.next = n;
    }
}
