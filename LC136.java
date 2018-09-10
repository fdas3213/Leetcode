import java.util.HashMap;

public class LC136 {
    public static int singleNumber(int[] nums) {
        HashMap<Integer, Integer> d = new HashMap<>();
        for (int val:nums){
            if (!d.containsKey(val)) d.put(val,1);
            else {
                int value = d.get(val);
                d.put(val, value+1);
            }
        }
        int single = 0;
        for(int val:nums){
            if (d.get(val) != 2) single = val;
        }
        return single;
    }

    public static void main(String[] args){
        int[] t1 = {2,2,1};
        System.out.println(singleNumber(t1));
        int[] t2 = {4,1,2,1,2};
        System.out.println(singleNumber(t2));
    }
}


