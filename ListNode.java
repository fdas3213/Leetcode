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

    public static String toString(ListNode h){
        String s = "[ ";
        while (h != null){
            s += h.val;
            s += " ";
            h = h.next;
        }
        s += "]";
        return s;
    }
}
