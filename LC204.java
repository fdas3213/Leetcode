public class LC204 {
    public static int countPrimes(int n) {
        if (n == 0) return 0;
        int count = 0;
        for (int i = 1; i < n; i++){
            if (isPrime(i)) count++;
        }
        return count;
    }

    private static boolean isPrime(int num){
        if ((num >2 && num%2 == 0) || num == 1) return false;
        // skip all even numbers because if it is divisible by a even number,
        // then it must be divisible by 2, but this is the first condition of the algorithm
        for (int i = 3; i <= (int)Math.sqrt(num); i+=2){
            if (num % i == 0) return false;
        }
        return true;
    }

    public static int bettersolution(int n){
        int count = 0;
        boolean[] prime = new boolean[n];
        for (int i = 2; i< n; i++){
            if (!prime[i]) {
                count ++;
                for (int j = i; i*j < n;j++){
                    prime[i*j] = true;
                }
            }
        }
        return count;
    }
    public static void main(String[] args){
        System.out.println(countPrimes(10));
        System.out.println(bettersolution(10));
    }
}
