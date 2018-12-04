import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;

public class LC49 {
    private static List<List<String>> groupAnagrams(String[] strs) {
        if(strs.length == 0 || strs == null) return new ArrayList<List<String>>();
        HashMap<String, List<String>> m = new HashMap<>();
        for (String s: strs){
            char[] arr = s.toCharArray();
            Arrays.sort(arr);
            String key = String.valueOf(arr);
            if (!m.containsKey(key)) m.put(key, new ArrayList<String>());
            m.get(key).add(s);
        }
        return new ArrayList<List<String>>(m.values());
    }

    private static List<List<String>> groupAnaFast(String[] strs){
        int[] primes = {2,3,5,7,11,13,17,19,23,29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101};
        HashMap<Integer, List<String>> hm = new HashMap<>();
        for (String s:strs){
            int product = 1;
            for (char c: s.toCharArray()){
                product *= primes[c - 'a'];
            }
            if(!hm.containsKey(product)) hm.put(product, new ArrayList<String>());
            hm.get(product).add(s);
        }
        return new ArrayList<List<String>>(hm.values());
    }

    public static void main(String[] args){
        String[] test = {"eat", "tea", "tan", "ate", "nat", "bat"};
        System.out.println(groupAnagrams(test));
    }
}
