import java.util.HashMap;

public class LC137 {
    private static int singleNumber(int[] nums){
        HashMap<Integer, Integer> hm = new HashMap<>();
        for (int n:nums){
            if (!hm.containsKey(n)) hm.put(n, 1);
            else hm.put(n, hm.get(n)+1);
        }
        int output = -1;
        for (int k: hm.keySet()){
            if (hm.get(k) != 3) output = k;
        }
        return output;
    }


    public static void main(String[] args){
        int[] t1 = {2,2,3,2};
        int[] t2 = {0,1,0,1,0,1,99};
        System.out.println(singleNumber(t1));
        System.out.println(singleNumber(t2));
    }
}
