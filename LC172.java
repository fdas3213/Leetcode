public class LC172 {
    public static int trailingZeroes(int n) {
        int count = 0;
        while(n > 0){
            count += n/5;
            n /=5;
        }
        return count;
    }

    public static void main(String[] args){
        System.out.println(trailingZeroes(3));
        System.out.println(trailingZeroes(5));
        System.out.println(trailingZeroes(13));
    }
}
