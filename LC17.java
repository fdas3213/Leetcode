/*
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

*/

import java.util.LinkedList;
import java.util.List;

public class LC17 {
    public static List<String> letterCombinations(String digits) {
        LinkedList<String> out = new LinkedList<>();
        if (digits.isEmpty()) return out;
        String[] mapping = new String[]{"0","1","abc","def","ghi","jkl","mno", "pqrs","tuv","wxyz"};
        out.add("");
        for (int i = 0; i < digits.length(); i++){
            int x = Character.getNumericValue(digits.charAt(i));
            while(out.peek().length() == i){
                String t = out.remove();
                for(char s: mapping[x].toCharArray()) out.add(t+s);
            }
        }
        return out;
    }

    public static void main(String[] args){
        System.out.println(letterCombinations("23"));
    }
}
