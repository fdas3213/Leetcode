import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class LC40 {
    public static List<List<Integer>> combinationSum2(int[] candidates, int target){
        Arrays.sort(candidates);
        List<List<Integer>> l = new ArrayList<>();
        backtrack(l, new ArrayList<>(), candidates, target, 0);
        return l;
    }

    private static void backtrack(List<List<Integer>> list, List<Integer> tempList, int[] nums, int remain, int start){
        if (remain < 0) return;
        else if (remain == 0) list.add(new ArrayList<>(tempList));
        else{
            for (int i = start; i < nums.length; i++){
                //add one condition to avoid duplicate
                if (i > start && nums[i] == nums[i-1]) continue;
                tempList.add(nums[i]);
                //System.out.println("i: " + i + " " + tempList);
                backtrack(list, tempList, nums, remain-nums[i], i+1);
                tempList.remove(tempList.size() - 1);
            }
        }
    }

    public static void main(String[] args){
        int[] t1 = {10,1,2,7,6,1,5};
        int[] t2 = {2,5,2,1,2};
        //System.out.println(combinationSum2(t1,8));
        System.out.println(combinationSum2(t2,5));
    }
}
