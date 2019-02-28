import java.util.List;
import java.util.ArrayList;
/*
Given a collection of distinct integers, return all possible permutations.
Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
 */

public class LC46 {

    private static List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> out = new ArrayList<>();
        backtrack(out, new ArrayList<>(), nums);
        return out;
    }

    private static void backtrack(List<List<Integer>> list, List<Integer> tempList, int[] nums){
        if (tempList.size() == nums.length) list.add(new ArrayList<>(tempList));
        else{
            for(int i = 0; i < nums.length; i++){
                //System.out.println("Before add, i: " + i + " " + tempList);
                if(tempList.contains(nums[i])) continue;
                tempList.add(nums[i]);
                //System.out.println("After add, i: " + i + " " + tempList);
                backtrack(list, tempList, nums);
                tempList.remove(tempList.size() - 1);
            }
        }

    }

    public static void main(String[] args){
        int[] t1 = {1,2,3};
        System.out.println(permute(t1));
    }
}
