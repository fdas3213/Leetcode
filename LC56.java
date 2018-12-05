import java.util.ArrayList;
import java.util.List;

public class LC56 {
    private static List<Interval> merge(List<Interval> intervals) {
        if(intervals.size() <= 1) return intervals;
        List<Interval> out = new ArrayList<>();
        for(int i = 0; i < intervals.size(); i++){
            Interval cur = intervals.get(i);
            for (int j = i+1; j < intervals.size(); j++){
                Interval comp = intervals.get(j);
                if (cur.end >= comp.start) {
                    Interval newone = new Interval(cur.start, comp.end);
                    out.add(newone);
                }
            }
        }
        /*
        Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
         */
    }

    public static void main(String[] args){

    }
}
