public class LC198 {
    public static int rob(int[] nums) {
        if (nums.length == 0) return 0;
        int[] dp = new int[nums.length+1];
        dp[0] = 0;
        dp[1] = nums[0];
        for (int i = 1; i <nums.length;i++){
            int val = nums[i];
            dp[i+1] = Math.max(val + dp[i-1], dp[i]);
        }
        return dp[nums.length];
    }

    public static void main(String[] args){

        int[] t1 = {1,2,3,1};
        int[] t2 = {2,7,9,3,1};
        int[] t3 = {2,1,1,2};

        System.out.println(rob(t1));
        System.out.println(rob(t2));
        System.out.println(rob(t3));

        int[] t4 = {1,3,1,3,100};
        System.out.println(rob(t4));



    }
}
