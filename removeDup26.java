import java.util.Arrays;

public class removeDup {
    public static void main(String[] args){
        int[] t1 = {1,1,2};
        System.out.println(Arrays.toString(removeDuplicates(t1)));
        System.out.println(Arrays.toString(removeDup(t1)));
        int[] t2 = {0,0,1,1,1,2,2,3,3,4};
        System.out.println(Arrays.toString(removeDuplicates(t2)));
        System.out.println(Arrays.toString(removeDup(t2)));

    }

    public static int[] removeDuplicates(int[] nums) {
        int i = 0, j = 0;
        while (i < nums.length){
            nums[j] = nums[i];
            do {
                i ++;
            }while ((i < nums.length) && (nums[i] == nums[j]));
            j ++;
        }
        return nums;
    }

    public static int[] removeDup(int[] nums){
        if(nums.length == 0) return nums;
        int out = nums[0];
        int l = 1;
        for (int i = 0; i < nums.length; i ++){
            if (out != nums[i]){
                out = nums[i];
                nums[l] = out;
                l ++;
            }
        }
        return nums;
    }
}
