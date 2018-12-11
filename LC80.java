public class LC80 {
    private static int removeDuplicates(int[] nums){
        int l = 1, dup = 1;
        for (int i = 1; i < nums.length;i++){
            if(nums[i-1] == nums[i] && dup < 2){
                nums[l++] = nums[i];
                dup++;
            }else if(nums[i-1] == nums[i] && dup>=2){
                dup++;
            }else{
                nums[l++] = nums[i];
                dup = 1;
            }
        }
        return l;
    }

    private static int sol2(int[] nums){
        int l = 0;
        for (int n : nums){
            if (l < 2 || nums[l-2] < n){
                nums[l++] = n;
            }
        }
        return l;
    }

    public static void main(String[] args){
        int[] t1 = {1,1,1,2,2,3};
        int[] t2 = {0,0,1,1,1,1,2,3,3};
        System.out.println(removeDuplicates(t1));
        System.out.println(removeDuplicates(t2));
    }
}
