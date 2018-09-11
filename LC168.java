
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
        }else{
            return convertToTitle(n/26) + Character.toString((char)((int)'A' + mod)) ;
        }
    }

    public static String sol(int n){
        StringBuilder s = new StringBuilder();
        while (n > 0){
            n--;
            int mod = n%26;
            s.append((char)((int)'A'+mod));
            n /= 26;
        }
        return s.reverse().toString();
    }

    public static void main(String[] args){
        System.out.println(convertToTitle(1));
        System.out.println(convertToTitle(28));
        System.out.println(convertToTitle(702));
        System.out.println(convertToTitle(52));
        System.out.println(convertToTitle(704));

        System.out.println(sol(1));
        System.out.println(sol(28));
        System.out.println(sol(702));
        System.out.println(sol(52));
        System.out.println(sol(704));
    }
}
