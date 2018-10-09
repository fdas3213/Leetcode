public class LC234 {
    public static boolean isPalindrome(ListNode head) {
        if (head == null) return true;
        //two pointers to help slow get to middle
        ListNode slow = head, fast = head;
        while (fast!= null && fast.next != null){
            slow = slow.next;
            fast = fast.next.next;
        }
        //reverse slow
        ListNode newhead = null;
        while(slow != null){
            ListNode next = slow.next;
            slow.next = newhead;
            newhead = slow;
            slow = next;
        }
        //compare
        fast = head;
        while(newhead != null){
            if(fast.val != newhead.val) return false;
            fast = fast.next;
            newhead = newhead.next;
        }
        return true;
    }

    //test cases
    public static void main(String[] args){
        ListNode l1 = new ListNode(1,new ListNode(2));
        ListNode l2 = new ListNode(1, new ListNode(2, new ListNode(2, new ListNode(1))));
        System.out.println(isPalindrome(l1));
        System.out.println(isPalindrome(l2));
    }
}
