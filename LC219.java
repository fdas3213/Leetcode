import java.util.HashMap;

public class LC219 {
    public static boolean containsNearbyDuplicate(int[] nums, int k) {
        if (nums.length == 0 || nums.length == 1) return false;
        for (int i = 0; i < nums.length-1; i++){
            for (int j = i+1; j < nums.length; j++){
                if (nums[i] == nums[j]){
                    if (j-i <= k) return true;
                }
            }
        }
        return false;
    }

    public static boolean solution2(int[] nums, int k) {
        HashMap<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++){
            if (map.containsKey(nums[i]) && (i - map.get(nums[i]) <= k)) return true;
            map.put(nums[i],i);
        }
        return false;
    }

    public static void main(String[] args){
        int[] t1 = {1,2,3,1};
        int[] t2 = {1,0,1,1};
        int[] t3 = {1,2,3,1,2,3};
        System.out.println(containsNearbyDuplicate(t1,3));
        System.out.println(containsNearbyDuplicate(t2,1));
        System.out.println(containsNearbyDuplicate(t3,2));
    }
}
