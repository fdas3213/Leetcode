import java.util.Arrays;
import java.util.HashMap;

public class LC1 {
    public static int[] twoSum(int[] nums, int target){
        int[] result = new int[2];
        HashMap<Integer, Integer> hm = new HashMap<>();
        for (int i=0; i < nums.length; i++){
            if (hm.containsKey(nums[i])) {
                result[0] = i;
                result[1] = hm.get(nums[i]);
            }
            hm.put(target - nums[i], i);
        }
        return result;
    }

    //unit test
    public static void main(String[] args){
        int[] test = {2,7,11,15};
        System.out.println(Arrays.toString(twoSum(test, 9)));
    }
}
