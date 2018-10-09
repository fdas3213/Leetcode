public class MyStack {
    private class ListNode{
        int val;
        ListNode next;
        ListNode(int x, ListNode n){
            val = x;
            next = n;
        }
    }

    //use a linkedlist data structure
    private ListNode stack;

    /** Initialize your data structure here. */
    public MyStack() {

    }

    /** Push element x onto stack. */
    public void push(int x) {
        if (stack == null) stack = new ListNode(x, null);
        else stack = new ListNode(x, stack);
    }

    /** Removes the element on top of the stack and returns that element. */
    public int pop() {
        int out = stack.val;
        stack = stack.next;
        return out;
    }

    /** Get the top element. */
    public int top() { return stack.val; }

    /** Returns whether the stack is empty. */
    public boolean empty() {
        return stack == null;
    }

    public static void main(String[] args){
        MyStack obj = new MyStack();
        obj.push(10);
        int param = obj.pop();
        System.out.println(param);
        System.out.println(obj.empty() == true);
    }

}
