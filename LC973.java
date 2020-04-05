import java.util.Arrays;
import java.util.PriorityQueue;

public class LC973 {
    public static int[][] kClosest(int[][] points, int K) {
        if (points.length == 0 || points == null) return points;
        int[][] res = new int[K][2];
        PriorityQueue<int[]> pq = new PriorityQueue<>((p1,p2) -> p2[0]*p2[0]-p1[0]*p1[0] + p2[1]*p2[1]-p1[1]*p1[1]);
        for(int i=0;i<points.length;i++){
            pq.offer(points[i]);
            if(pq.size() > K) pq.poll();
        }
        for(int i=0;i<K;i++){
            res[i] = pq.poll();
        }
        return res;
    }

    public static void main(String[] args){
        int[][] input = {{-1,3},{2,2}};
        int[][] out = kClosest(input,1);
        for (int[] sub : out){
            System.out.println(Arrays.toString(sub));
        }
    }
}