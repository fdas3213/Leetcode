public class MinStack {
    /** initialize your data structure here. */
    private class ListNode{
        int val;
        int minval;
        ListNode next;

        ListNode(int x, int min, ListNode n){
            val = x;
            minval = min;
            next = n;
        }
    }
    //using a Linkedlist data structure
    private ListNode stack;

    public void push(int x) {
        if (stack == null) stack = new ListNode(x,x,null);
        else stack = new ListNode(x,Math.min(stack.minval, x), stack);
    }

    public void pop() {
        stack = stack.next;
    }

    public int top() {
        return stack.val;
    }

    public int getMin() {
        return stack.minval;
    }

    public static void main(String[] args){
        MinStack obj = new MinStack();
        obj.push(2);
        obj.push(3);
        obj.push(1);
        System.out.println(obj.getMin());
        obj.pop();
        System.out.println(obj.top());
        System.out.println(obj.getMin());
    }
}

