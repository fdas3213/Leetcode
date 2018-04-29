import java.util.Arrays;

public class RemoveElement27 {

    public static void main(String[] args){
        int[] t1 = {3,2,2,3};
        int[] t2 = {0,1,2,2,3,0,4,2};
        System.out.println(Arrays.toString(removeElement(t1,3)));
        System.out.println(Arrays.toString(removeElement(t2,2)));
    }


    public static int[] removeElement(int[] nums, int val) {
        if (nums == null || nums.length == 0) return nums;
        int len = 0;
        for (int i = 0; i <nums.length; i++){
            if (nums[i] != val){
                nums[len] = nums[i];
                len ++;
            }
        }
        return nums;
    }


}
