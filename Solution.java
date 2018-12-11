import java.util.Arrays;
import java.util.List;
import java.util.ArrayList;

public class Solution {
    public static List<String> generateParenthesis(int n) {
        List<String> list = new ArrayList<String>();
        backtrack(list, "", 0, 0, n);
        return list;
    }

    private static void backtrack(List<String> list, String str, int open, int close, int max){
        System.out.println(str);
        if(str.length() == max*2){
            list.add(str);
            return;
        }
        if(open < max)
            backtrack(list, str+"(", open+1, close, max);
        if(close < open)
            backtrack(list, str+")", open, close+1, max);
    }

    private static int removeD(int[] nums){
        if (nums.length == 0) return 0;
        int l = 1;
        for (int i = 1; i < nums.length; i ++){
            if (nums[i-1] != nums[i]) nums[l++] = nums[i];
        }
        return l;
    }

    private static int removeE(int[] nums, int val){
        int l = 0;
        for (int i = 0; i < nums.length; i++){
            if (nums[i] != val) nums[l++] = nums[i];
        }
        return l;
    }

    private static int maxSubArray(int[] nums) {
        int[] rewards = new int[nums.length];
        rewards[0] = nums[0];
        int max = nums[0];
        for (int i = 1; i < nums.length; i++){
            rewards[i] = Math.max(rewards[i-1]+nums[i], nums[i]);
            if (rewards[i] > max) max = rewards[i];
        }
        return max;
    }

    private static boolean canJump(int[] nums){
        int max = 0;
        for (int i = 0; i < nums.length; i++){
            if (i > max) return false;
            max = Math.max(nums[i]+i, max);
        }
        return true;
    }

    private static int LC58(String s){
        if(s.length() == 0 || s == " ") return 0;
        int len = s.length();
        int k = 0;
        for (int i = len-1; i >= 0; i--){
            if(s.charAt(i) == ' ' && k > 0) return k;
            else if(s.charAt(i) != ' ') k++;
        }
        return k;
    }

    private static int[] plusOne(int[] digits) {
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

    private static String addBinary(String a, String b){
        StringBuilder out = new StringBuilder();
        int l1 = a.length()-1, l2 = b.length()-1;
        int mod = 0, sum;
        while(l1 >=0 || l2 >= 0){
            if(l1 >=0 && l2 >= 0) sum = (a.charAt(l1--) - '0') + (b.charAt(l2--)-'0') + mod;
            else if (l1 < 0 && l2 >= 0) sum = b.charAt(l2--) -'0' + mod;
            else sum = a.charAt(l1--)-'0' + mod;
            mod = sum /2;
            out.append(sum%2);
        }
        if (mod !=0) out.append(mod);
        return out.reverse().toString();
    }

    private static int climbStairs(int n) {
        if (n <= 2) return n;
        int sum = 0, two_step = 2, one_step = 1;
        for (int i = 2; i <n; i++){
            sum = one_step + two_step;
            one_step = two_step;
            two_step = sum;
        }
        return sum;
    }

    public static void print2dArray(int[][] test){
        StringBuilder s = new StringBuilder();
        s.append("[ " + '\n');
        for (int i = 0; i < test.length; i++){
            s.append(Arrays.toString(test[i])+'\n');
        }
        s.append("]");
        System.out.println(s.toString());
    }

    public static void sortColors(int[] nums) {

    }

    public static void main(String[] args){
        System.out.println(addBinary("11","1"));
        System.out.println(addBinary("1010","1011"));
    }
}
