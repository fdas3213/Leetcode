/*
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
 */
public class LC67 {
    public static String addBinary(String a, String b) {
        int l1 = a.length() - 1, l2 = b.length() -1;
        StringBuilder out = new StringBuilder();
        int over = 0;
        while (l1 >= 0 && l2 >= 0){
            int sum = Character.getNumericValue(a.charAt(l1--)) + Character.getNumericValue(b.charAt(l2--));
            if(sum == 2) {
                out.append(0);
                over = 1;
            }
            else out.append(sum);
        }
        return out.toString();
    }

    public static void main(String[] args){
        StringBuilder s = new StringBuilder();
        s.append(1);
        System.out.println(s.toString());
    }

}
