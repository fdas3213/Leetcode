public class LC55 {
    private static boolean canJump(int[] nums){
        int max = 0;
        for(int i = 0; i < nums.length; i++){
            if (i > max) return false;
            max = Math.max(nums[i]+i, max);
        }
        return true;
    }

    public static void main(String[] args){
        int[] t1 = {2,3,1,1,4};
        int[] t2= {3,2,1,0,4};
        System.out.println(canJump(t1));
        System.out.println(canJump(t2));
    }
}
