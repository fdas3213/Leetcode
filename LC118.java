import java.util.ArrayList;
import java.util.List;

public class LC118 {
    public static List<List<Integer>> generate(int numRows) {
        List<List<Integer>> outList = new ArrayList<>();
        for(int i = 0; i < numRows; i++){
            List<Integer> innerList = new ArrayList<>();
            for (int j = 0; j <= i; j++){
                if (j == 0 || j == i) {
                    innerList.add(1);
                }else{
                    int a = outList.get(i-1).get(j-1);
                    int b = outList.get(i-1).get(j);
                    innerList.add(a+b);
                }
            }
            outList.add(innerList);
        }
        return outList;
    }

    public static void main(String[] args){
        System.out.println(generate(5));
    }
}
