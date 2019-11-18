import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class LC18 {
    public static List<List<Integer>> fourSum(int[] nums, int target) {
        List<List<Integer>> list = new ArrayList<>();
        if (nums.length == 0) return list;
        Arrays.sort(nums);
        for(int i=0; i<nums.length-3;i++){
            if (i >0 && nums[i] == nums[i-1]) continue;
            for(int j=i+1;j<nums.length-2;j++){
                if(j>i+1 && nums[j]==nums[j-1])continue;
                int left = j+1, right = nums.length-1;
                while(left < right){
                    int sum = nums[i]+nums[j]+nums[left]+nums[right];
                    if (sum < target) left++;
                    else if (sum > target) right--;
                    else {
                        List<Integer> tmp = new ArrayList<>();
                        tmp.add(nums[i]);
                        tmp.add(nums[j]);
                        tmp.add(nums[left]);
                        tmp.add(nums[right]);
                        list.add(tmp);
                        while(left < right && nums[left]==nums[left+1]) left++;
                        while(left<right && nums[right]==nums[right-1])right--;
                        left++;
                        right--;
                    }
                }
            }
        }
        return list;
    }

    public static void main(String[] args){
        int[] t1 = {1,0,-1,0,-2,2};
        int target = 0;
        System.out.println(fourSum(t1,target));
    }
}
