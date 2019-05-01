public class LC125 {

    public static boolean isPalindrome(String s){
        if (s == "" || s == null) return false;
        int start = 0, end = s.length()-1;
        s = s.toLowerCase();
        while (start <= end){
            char char_s = s.charAt(start);
            char char_e = s.charAt(end);
            if (!Character.isLetterOrDigit(char_s)) start++;
            else if(!Character.isLetterOrDigit(char_e)) end--;
            else {
                if (char_s != char_e) return false;
                start++;
                end--;
            }
        }
        return true;
    }

    public static void main(String[] args){
        String t1 = "A man, a plan, a canal: Panama";
        System.out.println(isPalindrome(t1));
    }

}
