import java.util.HashSet;
import java.util.Set;

public class LC136 {
    public static int singleNumber(int[] nums) {
        Set<Integer> d = new HashSet<>();
        for (int val:nums){
            if (!d.add(val)) d.remove(val);
            else d.add(val);
        }
        int single = 0;
        for(int val:d){
            single = val;
        }
        return single;
    }

    private static int bitSolution(int[] nums){
        //using bitwise operation
        int out = 0;
        for (int n:nums){
            out ^= n;
        }
        return out;
    }

    public static void main(String[] args){
        int[] t1 = {2,2,1};
        System.out.println(singleNumber(t1));
        int[] t2 = {4,1,2,1,2};
        System.out.println(singleNumber(t2));
    }
}


