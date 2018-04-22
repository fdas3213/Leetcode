public class PalindromeNumber {

    public static void main(String[] args){
        int t = 121;
        int t1 = 10;
        int t2 = -121;
        int t3 = 0;
        System.out.println(Palindrome(t));
        System.out.println(Palindrome(t1));
        System.out.println(Palindrome(t2));
        System.out.println(Palindrome(t3));
    }

    public static Boolean Palindrome(int x){
        if (x < 0) return false;
        int out = 0;
        int copy = x;
        while (x != 0){
            int mod = x % 10;
            out = out * 10 + mod;
            x /= 10;
        }
        return copy == out;
    }
}
