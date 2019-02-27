import java.util.ArrayList;
import java.util.List;

public class LC39 {
    public static List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>> out = new ArrayList<>();
        backtrack(out, new ArrayList<>(), candidates, target, 0);
        return out;
    }

    private static void backtrack(List<List<Integer>> list, List<Integer> tempList, int[] nums, int remain, int start){
        if (remain < 0) return;
        else if(remain == 0) list.add(new ArrayList<>(tempList));
        else{
            for(int i = start; i < nums.length; i++){
                tempList.add(nums[i]);
                //System.out.println("i: " + i + " " + tempList);
                backtrack(list, tempList, nums, remain-nums[i], i);
                tempList.remove(tempList.size()-1);
            }
        }
    }

    public static void main(String[] args){
        int[] t1 = {2,3,6,7};
        int[] t2 = {2,3,5};
        System.out.println(combinationSum(t1, 7));
    }
}
