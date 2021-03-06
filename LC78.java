import java.util.Arrays;
import java.util.List;
import java.util.ArrayList;

public class LC78 {
    public static List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> out = new ArrayList<>();
        Arrays.sort(nums);
        backtrack(out, new ArrayList<>(), nums,0);
        return out;
    }

    private static void backtrack(List<List<Integer>> list, List<Integer> tempList, int[] nums, int start){
        list.add(new ArrayList<>(tempList));
        for (int i = start; i < nums.length; i++){
            tempList.add(nums[i]);
            backtrack(list, tempList, nums, i+1);
            tempList.remove(tempList.size()-1);
        }
    }

    public static void main(String[] args){
        int[] t1 = {1,2,3};
        System.out.println(subsets(t1));
    }

}
