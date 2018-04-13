import java.util.Stack;

public class valid_parenthesis {
    public static void main(String[] args){
        String s1 = "([)]";
        String s2 = "{}([]){[]}";
        System.out.println("String s1 is: " + isValid(s1));
        System.out.println("String s2 is: " + isValid(s2));
    }

    public static boolean isValid(String s){
        Stack<Character> stack = new Stack<Character>();
        for (char c : s.toCharArray()) {
            if (c == '('){
                stack.push(')');
            }else if(c == '['){
                stack.push(']');
            }else if(c == '{'){
                stack.push('}');
            }else if (stack.isEmpty() || stack.pop() != c){
                return false;
            }
        }
        return stack.isEmpty();
    }
}
