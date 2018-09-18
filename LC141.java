public class LC141 {
    public boolean hasCycle(ListNode head) {
        if (head == null) return false;
        ListNode s1 = head.next;
        ListNode s2 = head;
        while (s1 != null && s2 != null && s1.next != null){
            if(s1 == s2) return true;
            s1 = s1.next.next;
            s2 = s2.next;
        }
        return false;
    }
}
