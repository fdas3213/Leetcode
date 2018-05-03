import java.util.Arrays;
import java.lang.Math;

public class plusone66 {
    public static void main(String[] args){
        int[] t1 = {1,2,3};
        int[] t2 = {4,3,2,1};
        int[] t3 = {9};
        System.out.println(Arrays.toString(plusone(t1)));
        System.out.println(Arrays.toString(plusone(t2)));
        System.out.println(Arrays.toString(plusone(t3)));
    }

    public static int[] plusone(int[] digits){
        for (int i = digits.length -1; i >= 0; i --){
            if (digits[i] < 9) {
                digits[i] ++;
                return digits;
            }
            digits[i] = 0;
        }
        int[] out = new int[digits.length + 1];
        out[0] = 1;
        return out;
    }
}
