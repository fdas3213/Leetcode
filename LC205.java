/*
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true
Note:
You may assume both s and t have the same length.
 */
import java.util.HashMap;

public class LC205 {
    public static boolean isIsomorphic(String s, String t) {
        if (s == null && t == null) return true;
        HashMap<Character,Character> cmap = new HashMap<>();
        for(int i = 0; i < s.length(); i++){
            char s_c = s.charAt(i);
            char t_c = t.charAt(i);
            if (!cmap.containsKey(s_c)) {
                if (!cmap.containsValue(t_c)) cmap.put(s_c, t_c);
                else return false;
            }
            else {
                if (t_c != cmap.get(s_c)) return false;
            }
        }
        return true;
    }

    public static void main(String[] args){
        String ts_1 = "egg", tt_1 = "add";
        String ts_2 = "foo", tt_2 = "bar";
        String ts_3 = "paper", tt_3 = "title";
        String ts_4 = "ab", tt_4 = "aa";
        System.out.println(isIsomorphic(ts_1, tt_1));
        System.out.println(isIsomorphic(ts_2, tt_2));
        System.out.println(isIsomorphic(ts_3, tt_3));
        System.out.println(isIsomorphic(ts_4, tt_4));
    }
}
