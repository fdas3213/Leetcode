import java.util.Arrays;
import java.util.List;
import java.util.ArrayList;

public class LC47 {
    public static List<List<Integer>> permuteUnique(int[] nums){
        List<List<Integer>> out = new ArrayList<>();
        boolean[] used = new boolean[nums.length];
        if (nums.length == 0 || nums == null) return out;
        Arrays.sort(nums);
        backtracking(out, new ArrayList<>(), nums, used);
        return out;
    }

    private static void backtracking(List<List<Integer>> list, List<Integer> tempList, int[] nums, boolean[] used){
        if (tempList.size() == nums.length) list.add(new ArrayList<>(tempList));
        else{
            for (int i = 0; i < nums.length; i++){
                if (used[i]) continue;
                if(i>0 && nums[i] == nums[i-1] && !used[i-1]) continue;
                used[i] = true;
                tempList.add(nums[i]);
                backtracking(list, tempList, nums, used);
                used[i] = false;
                tempList.remove(tempList.size()-1);
            }
        }
    }

    public static void main(String[] args){
        int[] nums = {1,1,2};
        List<List<Integer>> ans = permuteUnique(nums);
        System.out.println(ans);
    }
}
