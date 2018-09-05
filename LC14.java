public class LC14 {
    public static String longestCommonPrefix(String[] strs) {
        if (strs == null || strs.length == 0) return "";
        String s = strs[0];
        for (int i = 1;i< strs.length;i++){
            int j = 0;
            String inner_s = "";
            while (j < Math.min(s.length(), strs[i].length()) && s.charAt(j) == strs[i].charAt(j)){
                inner_s += s.charAt(j++);
            }
            s = inner_s;
        }
        return s;
    }

    public static String longestCommonPrefixEasy(String[] strs){
        if (strs == null || strs.length == 0) return "";
        String s = strs[0];
        int i = 1;
        while (i < strs.length){
            while(strs[i].indexOf(s) != 0){
                s = s.substring(0, s.length()-1);
            }
            i++;
        }
        return s;
    }
    public static void main(String[] args){
        String[] t1 = {"flower", "flow","flight"};
        String[] t2 = {"dog", "racecar", "car"};

        System.out.println(longestCommonPrefix(t1));
        System.out.println(longestCommonPrefix(t2));
        System.out.println(longestCommonPrefixEasy(t1));
    }
}
