public class LC26 {
    public static int removeDuplicates(int[] nums){
        if (nums.length <= 1) return nums.length;
        int l = 1;
        for (int i = 1; i < nums.length; i++){
            if (nums[i-1] != nums[i]) nums[l++] = nums[i];
        }
        return l;
    }

    public static void main(String[] args){
        int[] t1 = {1,1,2};
        int[] t2= {0,0,1,1,1,2,2,3,3,4};
        System.out.println(removeDuplicates(t1));
        System.out.println(removeDuplicates(t2));
    }
}
