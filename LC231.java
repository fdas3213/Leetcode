public class LC231 {
    public static boolean isPowerOfTwo(int n) {
        if(n < 1) return false;
        while (n > 0){
            if(n>1 && n%2 != 0) return false;
            n /= 2;
        }
        return true;
    }

    public static void main(String[] args){
        //test cases
        int n1 = 1;
        int n2 = 16;
        int n3 = 218;
        System.out.println(n1 + " power of 2? " + isPowerOfTwo(n1));
        System.out.println(n2 + " power of 2? " + isPowerOfTwo(n2));
        System.out.println(n3 + " power of 2? " + isPowerOfTwo(n3));
    }
}
