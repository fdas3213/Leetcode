import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class LC56 {
    private static List<Interval> merge(List<Interval> intervals) {
        if (intervals.size() <= 1) return intervals;
        List<Interval> out = new ArrayList<>();
        int n = intervals.size();
        int[] start = new int[n];
        int[] end = new int[n];
        for (int i = 0; i < n; i++){
            start[i] = intervals.get(i).start;
            end[i] = intervals.get(i).end;
        }
        Arrays.sort(start);
        Arrays.sort(end);
        for(int i = 0, j =0; i < n;i++){
            if(i == n-1 || start[i+1]>end[i]){
                out.add(new Interval(start[j], end[i]));
                j = i+1;
            }
        }
        return out;
    }

    public static void main(String[] args){
        Interval t1 = new Interval(1,3);
        Interval t2 = new Interval(2,6);
        Interval t3 = new Interval(8,10);
        Interval t4 = new Interval(15,18);
        List<Interval> testinterval = new ArrayList<>();
        testinterval.add(t1);
        testinterval.add(t2);
        testinterval.add(t3);
        testinterval.add(t4);
        System.out.println(merge(testinterval));
    }
}
