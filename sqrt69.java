import java.lang.Math;

public class sqrt69 {
    public static void main(String[] args){
        System.out.println("Square root of 8: " + mySqrt(8));
        System.out.println("Square root of 10000: " + mySqrt(10000));
        System.out.println("Square root of 11: " + mySqrt(11));
    }

    public static int mySqrt(int x){
        if (x == 0 || x == 1) return x;
        int out = 0;
        for (int i = 1; i * i <= x; i ++){
            if (i * i <= x) {
                out = i;
            }
        }
        return out;
    }
}
