public class LC134 {
    public static int canCompleteCircuit(int[] gas, int[] cost) {
        //loop over all indices and see if at any index we can circulate
        int out = -1, l = gas.length;
        for (int i = 0; i<l; i++){
            int remain = 0;
            for (int j = i; j < i+l; j++){
                remain += gas[j%l];
                remain -= cost[j%l];
                if(remain < 0) break;
            }
            if (remain >= 0) return i;
        }
        return out;
    }

    public static int fastSolution(int[] gas, int[] cost){
        int total = 0;
        // if sum of gas < sum of cost, then there is no solution
        for (int i = 0; i < gas.length; i++ ){
            total += gas[i] -cost[i];
        }
        if (total < 0) return -1;
        int start = 0, accumulate = 0;
        for (int i = 0; i < gas.length; i++){
            int curGas = gas[i] - cost[i];
            if (accumulate + curGas < 0){
                start = i + 1;
                accumulate = 0;
            }else accumulate += curGas;
        }
        return start;
    }

    public static void main(String[] args){
        int[] g1 = {1,2,3,4,5};
        int[] c1 = {3,4,5,1,2};
        System.out.println(canCompleteCircuit(g1,c1));
        int[] g2 = {2,3,4};
        int[] c2 = {3,4,3};
        System.out.println(canCompleteCircuit(g2,c2));
        int[] g3 = {1,2,3,4,5,5,70};
        int[] c3 = {2,3,4,3,9,6,2};
        System.out.println(canCompleteCircuit(g3,c3));
    }
}
