public class LC9 {
    public static boolean isPalindrome(int x) {
        if (x < 0) return false;
        int n = x;
        int r = 0;
        while (x != 0){
            r = r*10 + x%10;
            x = x/10;
        }
        return r == n;
    }

    public static void main(String[] args){
        int t1 = 121;
        int t2 = -121;
        int t3 = 10;
        System.out.println(isPalindrome(t1));
        System.out.println(isPalindrome(t2));
        System.out.println(isPalindrome(t3));
    }
}
