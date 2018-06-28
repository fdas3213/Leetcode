import java.util.Arrays;
import java.util.HashMap;

public class anagram242 {
    //selection sort and insertion sort all run out of time
    public static boolean isAnagram(String s, String t){
        if(s.length() != t.length()) return false;
        //create an array of length 26
        int[] out = new int[26];
        for (int i = 0; i < s.length(); i++) {
            out[s.charAt(i)-'a'] ++;
        }
        for (int j = 0; j < t.length(); j++) {
            out[t.charAt(j)-'a'] --;
        }
        for(int n:out){
            if (n != 0) return false;
        }
        return true;
    }


    public static void main(String[] args){
        System.out.println(isAnagram("anagram","nagaram"));
        System.out.println(isAnagram("rat","car"));

    }

}
