import java.util.Arrays;
import java.util.List;

public class add2nums {

    public static ListNode addTwoNumbers(ListNode l1, ListNode l2){
        ListNode prev,result = new ListNode(0); //prev in only declared of type ListNode, but not initialized yet
        prev = result;
        int carry = 0;

        while (l1 != null || l2 != null || carry != 0){
            /* while at least one of the three conditions are met, the loop continues */
            if (l1 != null){
                carry += l1.val;
                l1 = l1.next;
            }
            if (l2 != null){
                carry += l2.val;
                l2 = l2.next;
            }
            prev.next = new ListNode(carry % 10);
            carry /= 10;
            prev = prev.next;
        }

        return result.next;
    }

    public static String toString(ListNode l){
        String s = "[ ";
        while (l != null){
            s = s + Integer.toString(l.val) + " ";
            l = l.next;
        }
        s += "]";
        return s;
    }
    public static void main(String[] args){
        ListNode l1 = new ListNode(9);
        ListNode l2 = new ListNode(1, new ListNode(9, new ListNode(9, new ListNode(9))));
        System.out.println(toString(addTwoNumbers(l1,l2)));

        System.out.println(18 / 10);

    }


}
