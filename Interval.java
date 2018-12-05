public class Interval {
    int start;
    int end;

    Interval() {
        start = 0;
        end = 0;
    }

    Interval(int s, int e) {
        start = s;
        end = e;
    }

    public static String toString(Interval interval){
        StringBuilder s = new StringBuilder();
        s.append("[");
        s.append(interval.start);
        s.append(",");
        s.append(interval.end);
        s.append("]");
        return s.toString();
    }
}
