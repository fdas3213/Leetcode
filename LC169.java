import java.util.HashMap;

public class LC169 {
    public static int majorityElement(int[] nums) {
        //using hashtable
        HashMap<Integer, Integer> hm = new HashMap<>();
        int majority = 0;
        for(int val:nums){
            if (!hm.containsKey(val)) hm.put(val, 1);
            else hm.put(val, hm.get(val)+1);
            if (hm.get(val) > nums.length/2){
                majority = val;
                break;
            }
        }
        return majority;
    }

    public static void main(String[] args){
        int[] arr1 = {3,2,3};
        int[] arr2 = {2,2,1,1,1,2,2};
        int[] arr3 = {1};
        System.out.println(majorityElement(arr1));
        System.out.println(majorityElement(arr2));
        System.out.println(majorityElement(arr3));
    }
}
