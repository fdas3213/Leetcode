public class LC7 {
    public static int reverse(int x) {
        long r = 0;
        while(x != 0){
            r = r*10 + x % 10;
            x /= 10;
            if (r > Integer.MAX_VALUE || r < Integer.MIN_VALUE) return 0;
        }
        return (int) r;
    }

    public static void main(String[] args){
        int t1 = 123;
        int t2 = -123;
        int t3 = 120;
        System.out.println(reverse(t1));
        System.out.println(reverse(t2));
        System.out.println(reverse(t3));
    }
}

