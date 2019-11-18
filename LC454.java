import java.util.HashMap;

public class LC454 {
    public static int fourSumCount(int[] A, int[] B, int[] C, int[] D) {
        int count = 0;
        HashMap<Integer, Integer> hm = new HashMap<>();
        for(int i =0;i<A.length;i++){
            for(int j =0;j<B.length;j++){
                int tmp =A[i]+B[j];
                if(hm.containsKey(tmp)){
                    hm.put(tmp, hm.get(tmp)+1);
                }else {
                    hm.put(tmp,1);
                }
            }
        }

        for(int i=0;i<C.length;i++){
            for(int j =0;j<D.length;j++){
                int rev = -(C[i]+D[j]);
                if(hm.containsKey(rev)) count += hm.get(rev);
            }
        }
        return count;
    }

    public static void main(String[] args){
        int[] A = {1,2};
        int[] B = {-2,-1};
        int[] C = {-1,2};
        int[] D = {0,2};
        System.out.println(fourSumCount(A,B,C,D));
    }
}
