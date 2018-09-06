import java.util.Arrays;

public class LC66 {
    public static int[] plutOne(int[] digits){
        int[] out = new int[digits.length];
        int reminder = 1;
        for (int k = digits.length-1; k >= 0; k--){
            int sum = digits[k] + reminder;
            if (reminder != 0) reminder = 0;
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
        System.out.println(Arrays.toString(plutOne(t1)));
        int[] t2= {4,3,2,1};
        System.out.println(Arrays.toString(plutOne(t2)));
        int[] t3 = {8,9,9,9};
        System.out.println(Arrays.toString(plutOne(t3)));
        int[] t4 = {9,9,9};
        System.out.println(Arrays.toString(plutOne(t4)));
    }
}

