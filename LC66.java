import java.util.Arrays;

public class LC66 {
    public static int[] plusOne(int[] digits){
        int[] out = new int[digits.length];
        int reminder = 1;
        for (int k = digits.length-1; k >= 0; k--){
            int sum = digits[k] + reminder;
            reminder = 0;
            if (sum == 10) {
                out[k] = 0;
                reminder++;
            }else out[k] = sum;
        }
        if (reminder == 0) return out;
        else {
            int[] newout = new int[digits.length + 1];
            newout[0] = reminder;
            return newout;
        }
    }

    private static int[] Solution3(int[] digits) {
        int n = digits.length - 1;
        if(digits[n] + 1 < 10){
            digits[n] ++;
            return digits;
        }
        int mod = (digits[n]+1)/10;
        for (int i = n; i>=0; i--){
            int sum = digits[i] + mod;
            mod = sum / 10;
            digits[i] = sum%10;
        }
        if(digits[0] != 0) return digits;
        else{
            int[] output = new int[digits.length+1];
            output[0] = 1;
            return output;
        }
    }

    public static int[] easysolution(int[] digits){
        for (int i = digits.length-1; i >= 0; i++){
            if(digits[i] < 9) {
                digits[i] ++;
                return digits;
            }
            digits[i] = 0;
        }
        int[] out = new int[digits.length+1];
        out[0] = 1;
        return out;
    }

    public static void main(String[] args){
        int[] t1= {1,2,3};
        System.out.println(Arrays.toString(plusOne(t1)));
        int[] t2= {4,3,2,1};
        System.out.println(Arrays.toString(plusOne(t2)));
        int[] t3 = {8,9,9,9};
        System.out.println(Arrays.toString(plusOne(t3)));
        int[] t4 = {9,9,9};
        System.out.println(Arrays.toString(plusOne(t4)));
    }
}

