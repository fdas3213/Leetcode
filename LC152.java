import java.util.Arrays;

public class LC152 {
    public static int maxProduct(int[] nums){
        int max = nums[0];
        int[] dp = new int[nums.length];
        int[] product = new int[nums.length];
        dp[0] = nums[0];
        product[0] = nums[0];
        for (int i = 1; i < nums.length;i++){
            dp[i] = Math.max(Math.max(dp[i-1]*nums[i], product[i-1]*nums[i]), nums[i]);
            product[i] = Math.min(Math.min(dp[i-1]*nums[i], product[i-1]*nums[i]), nums[i]);
            max = Math.max(max, dp[i]);
        }
        return max;
    }

    public static void main(String[] args){
        int[] t1 = {2,3,-2,4};
        int[] t2 = {2,-5,-2,-4,3};
        int[] t3 = {-2,3,-4};
        System.out.println(maxProduct(t1));
        System.out.println(maxProduct(t2));
        System.out.println(maxProduct(t3));
    }
}
