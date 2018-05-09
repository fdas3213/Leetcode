public class climbstar70 {
    public static void main(String[] args){
        int t1 = 4;
        int t2 = 10;
        System.out.println(climbStairs(t1));
        System.out.println(climbStairs(t2));
    }

    public static int climbStairs(int n) {
        if (n <= 0) return 0;
        if (n == 1 || n == 2) return n;

        int sum = 0;
        int one_step = 2;
        int two_step = 1;

        for (int i = 2; i < n; i ++){
            sum = one_step + two_step;
            two_step = one_step;
            one_step = sum;
        }
        return sum;
    }
}
