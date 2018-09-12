import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class LC15 {
    public static List<List<Integer>> threeSum(int[] nums){
        List<List<Integer>> listSolution = new ArrayList<>();
        Arrays.sort(nums);
        for (int i =0; i<nums.length -2;i++){
            int start = i+1, end = nums.length-1;
            while(start < end){
                int sum = nums[i] + nums[start] + nums[end];
                if (sum < 0) start++;
                else if (sum > 0) end--;
                else {
                    List<Integer> solution = new ArrayList(3);
                    solution.add(nums[i]);
                    solution.add(nums[start]);
                    solution.add(nums[end]);
                    if (!listSolution.contains(solution)) listSolution.add(solution);
                    start++;
                    end--;
                }
            }
        }
        return listSolution;
    }

    public static void main(String[] args){
        int[] t1 = {-1, 0, 1, 2, -1, -4};
        System.out.println(threeSum(t1));
        int[] t2 = {3,0,-2,-1,1,2};
        System.out.println(threeSum(t2));
    }
}
