public class MyQueue {
    /** Initialize your data structure here. */
    private class ListNode{
        int val;
        ListNode next;
        ListNode(int x, ListNode n){
            val = x;
            next = n;
        }
    }
    private ListNode head,tail;

    /** Push element x to the back of queue. */
    public void push(int x) {
        ListNode oldtail = tail;
        tail = new ListNode(x,null);
        if(empty()) head = tail;
        else oldtail.next = tail;
    }

    /** Removes the element from in front of queue and returns that element. */
    public int pop() {
        int out = head.val;
        head = head.next;
        if(empty()) tail = null;
        return out;
    }

    /** Get the front element. */
    public int peek() {
        return head.val;
    }

    /** Returns whether the queue is empty. */
    public boolean empty() {
        return head == null;
    }

    public static void main(String[] args){
        //unit test
        MyQueue obj = new MyQueue();
        obj.push(1);
        obj.pop();
        obj.push(2);
        System.out.println(obj.peek());
    }
}
