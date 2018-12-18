import java.util.Stack;

public class LC150 {
    public static int evalRPN(String[] tokens) {
        Stack<Integer> nums = new Stack<>();
        int result;
        for (String s: tokens){
            if(s.equals("+") || s.equals("*") || s.equals("-") || s.equals("/")) {
                int first = nums.pop();
                int second = nums.pop();
                switch (s){
                    case "+":
                        result = first+second;
                        break;
                    case "*":
                        result = first * second;
                        break;
                    case "-":
                        result = second - first;
                        break;
                    default: result = second / first;
                }
                nums.push(result);
            }else {
                nums.push(Integer.parseInt(s));
            }
        }
        return nums.pop();
    }


    public static void main(String[] args){
        String[] t1 = {"2","1","+","3","*"};
        System.out.println(evalRPN(t1));
        String[] t2 = {"4", "13", "5", "/", "+"};
        System.out.println(evalRPN(t2));
        String[] t3 = {"10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"};
        System.out.println(evalRPN(t3));
    }
}
