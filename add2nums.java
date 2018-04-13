public class add2nums {

    public ListNode addTwoNumbers(ListNode l1, ListNode l2){
        if(l1 == null) return l2;
        if(l2 == null) return l1;
        if(l1 == null && l2 == null) return null;

        int num1 = 0;
        int num2 = 0;

        while (l1 != null){
            num1 = num1 * 10 + l1.val;
            l1 = l1.next;
        }
        while (l2 != null){
            num2 = num2 * 10 + l2.val;
            l2 = l2.next;
        }

        int total = num1 + num2;
        ListNode result = new ListNode(0);
        ListNode prev = result;
        while (total != 0){
            prev.next = new ListNode(total % 10);
            total /= 10;
            prev = prev.next;
        }
        return result.next;
    }
    public static void main(String[] args){
        int i = 1;
        i *= 10;
        System.out.println("i: " + i);
        int j = 807;
        System.out.println("j / 10: " + j/10);
        System.out.println("j % 10: " + j%10);
    }
}
