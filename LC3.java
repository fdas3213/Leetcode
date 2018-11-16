public class LC3 {
    public static int lengthOfLongestSubstring(String s){
        if (s.length() == 0) return 0;
        String out = "";
        int max = 0;
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            int idx = out.indexOf(c);
            if (idx == -1) out += c;
            else out = out.substring(idx + 1) + c;
            if (out.length() > max) max = out.length();
        }
        return max;
    }

    public static void main(String[] args){
        String s1 = "abcabcbb";
        String s2 = "bbbbb";
        String s3 = "pwwkew";
        String s4 = "au";

        System.out.println(lengthOfLongestSubstring(s1));
        System.out.println(lengthOfLongestSubstring(s2));
        System.out.println(lengthOfLongestSubstring(s3));
        System.out.println(lengthOfLongestSubstring(s4));

    }
}
