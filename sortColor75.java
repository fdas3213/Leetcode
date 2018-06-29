import java.util.Arrays;

public class sortColor75 {
    //Use insertion sort
    public static void sortColors(int[] nums) {
        for (int i = 1; i <nums.length; i++){
            int j = i;
            while (j > 0 && nums[j-1] > nums[j]){
                int tmp = nums[j];
                nums[j] = nums[j-1];
                nums[j-1] = tmp;
                j--;
            }
        }
    }

    public static void main(String[] args){
        int[] test = {2,0,2,1,1,0};
        sortColors(test);
        System.out.println(Arrays.toString(test));
    }
}
