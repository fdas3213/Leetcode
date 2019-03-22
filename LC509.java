public class LC509 {
    public static int fib(int N) {
        if (N <= 0) return 0;
        if (N == 1) return N;
        int sum = 0, onestep = 1, twostep = 0;
        for (int i = 2; i <= N; i++){
            sum = onestep + twostep;
            twostep = onestep;
            onestep = sum;
        }
        return sum;
    }

    public static void main(String[] args){
        System.out.println(fib(2));
        System.out.println(fib(3));
        System.out.println(fib(4));
    }
}
