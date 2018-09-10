/*
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB
    ...
Example 1:

Input: 1
Output: "A"
Example 2:

Input: 28
Output: "AB"
Example 3:

Input: 701
Output: "ZY"
 */
public class LC168 {
    public static String convertToTitle(int n) {
        if (n == 0) return null;
        int div;
        int mod = (n-1) % 26;
        if (n <= 26) return Character.toString((char)((int)'A' + mod));
        else if (n > 26 && n <= 26*27){
            if (n%26 == 0) div = (n-1)/26 -1;
            else div = n/26 -1;
            return Character.toString((char)((int)'A' + div)) + Character.toString((char)((int)'A'+mod));
        }
        else
    }

    public static void main(String[] args){
        System.out.println(convertToTitle(1));
        System.out.println(convertToTitle(28));
        System.out.println(convertToTitle(702));
        System.out.println(convertToTitle(52));
    }
}
