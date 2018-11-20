import java.util.Arrays;

public class LC16 {
    public static int threeSumClosest(int[] nums, int target) {
        Arrays.sort(nums);
        int init = nums[0] + nums[1] + nums[nums.length - 1];
        for (int i = 0; i <nums.length - 2; i++){
            int start = i + 1, end = nums.length - 1;
            while (start < end){
                int sum = nums[start] + nums[end] + nums[i];
                if (sum < target) start++;
                else if (sum > target) end--;
                else return sum;
                if (Math.abs(sum - target) < Math.abs(init - target)){
                    init = sum;
                }
            }
        }
        return init;
    }

    public static void main(String[] args){
        int[] l = {-1,2,1,4};
        System.out.println(threeSumClosest(l,1));
    }
}
