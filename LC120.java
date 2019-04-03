import java.util.ArrayList;
import java.util.List;

public class LC120 {
    public static int minimumTotal(List<List<Integer>> triangle) {
        if (triangle == null || triangle.size() == 0) return 0;
        //bottom to top DP
        int size = triangle.size();
        int n = triangle.get(size-1).size();
        int[] dp = new int[n];
        for (int i = 0; i < n; i++) {
            dp[i] = triangle.get(size-1).get(i);
        }
        for (int i = n-2; i >= 0; i--){
            List<Integer> cur = triangle.get(i);
            for (int j = 0; j < cur.size(); j++){
                dp[j] = Math.min(dp[j], dp[j+1]) + cur.get(j);
            }
        }
        return dp[0];
    }

    public static void main(String[] args){
        List<List<Integer>> l = new ArrayList<>();
        List<Integer> t1 = new ArrayList<>();
        t1.add(2);
        l.add(t1);
        List<Integer> t2 = new ArrayList<>();
        t2.add(3);
        t2.add(4);
        l.add(t2);
        List<Integer> t3 = new ArrayList<>();
        t3.add(6);
        t3.add(5);
        t3.add(7);
        l.add(t3);
        List<Integer> t4 = new ArrayList<>();
        t4.add(4);
        t4.add(1);
        t4.add(8);
        t4.add(3);
        l.add(t4);
        System.out.println(minimumTotal(l));
    }
}
