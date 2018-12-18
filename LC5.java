public class LC5 {
    /*
    public static String longestPalindrome(String s){
        String out = "";
        String inner = "";
        for (int i = 0; i<s.length(); i++){
            char c = s.charAt(i);
            inner += c;
            if (isPalindrome(inner)) {
                if (out.length() < inner.length()) out = inner;
            }
            else{
                while (!isPalindrome(inner))
            }
        }
    }
    */
    private static Boolean isPalindrome(String s){
        if (s.length() == 1) return true;
        int i = 0;
        int j = s.length() - 1;
        while (i <= j){
            if (s.charAt(i) != s.charAt(j)) return false;
            i ++;
            j --;
        }
        return true;
    }

    public static void main(String[] args){
        String s = "bab";
        String s1 = "xiao";
        System.out.println(isPalindrome(s));
        System.out.println(isPalindrome(s1));
    }
}
