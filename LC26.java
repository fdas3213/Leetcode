public class LC26 {
    public static int removeDuplicates(int[] nums){
        int start = 0, i = 0;
        while (i < nums.length) {
            nums[start] = nums[i];
            do {
                i++;
            } while (i < nums.length && nums[i] == nums[start]);
            start++;
        }
        return start;
    }

    public static void main(String[] args){
        int[] t1 = {1,1,2};
        int[] t2= {0,0,1,1,1,2,2,3,3,4};
        System.out.println(removeDuplicates(t1));
        System.out.println(removeDuplicates(t2));
    }
}
