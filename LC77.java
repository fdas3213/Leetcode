import java.util.List;
import java.util.ArrayList;

public class LC77 {
    public static List<List<Integer>> combine(int n, int k){
        List<List<Integer>> out = new ArrayList<>();
        backtrack(out, new ArrayList<Integer>(), 1,n,k);
        return out;
    }

    private static void backtrack(List<List<Integer>> list, List<Integer> tempList, int start, int n, int k){
        if(k == 0){
            list.add(new ArrayList<Integer>(tempList));
            return;
        }
        for (int i = start; i <= n; i++){
            tempList.add(i);
            backtrack(list, tempList, i+1, n, k-1);
            tempList.remove(tempList.size()-1);
        }
    }

    public static void main(String[] args){
        System.out.println(combine(4,2));
    }
}
