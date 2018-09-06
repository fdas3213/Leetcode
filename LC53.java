import java.util.Arrays;

public class LC53 {
    public static int maxSubArrat(int[] nums){
        int[] reward = new int[nums.length];
        int max = nums[0];
        reward[0] = nums[0];
        for(int i = 1; i < nums.length; i++){
            reward[i] = Math.max(reward[i-1] + nums[i], nums[i]);
            max = Math.max(reward[i], max);
        }
        System.out.println(Arrays.toString(reward));
        return max;
    }
    public static void main(String[] args){
        int[] l1 = {-2,1,-3,4,-1,2,1-5,4};
        System.out.println(maxSubArrat(l1));
    }
}
