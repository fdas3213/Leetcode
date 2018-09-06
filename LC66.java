import java.util.Arrays;

/*
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.

*/
public class LC66 {
    public static int[] plutOne(int[] digits){
        int num = 0;
        int l = 0;
        for (int i = 0; i < digits.length;i++){
            num = num * 10 + digits[i];
            l++;
        }
        num ++;

        int[] out = new int[l];
        for (int k = l-1; k >= 0; k--){
            out[k] = num % 10;
            num /= 10;
        }
        return out;
    }

    public static void main(String[] args){
        int[] t1= {1,2,3};
        System.out.println(Arrays.toString(plutOne(t1)));
        int[] t2= {4,3,2,1};
        System.out.println(Arrays.toString(plutOne(t2)));
        int[] t3 = {8,9,9,9};
        System.out.println(Arrays.toString(plutOne(t3)));
    }
}

