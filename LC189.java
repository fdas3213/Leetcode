import java.util.Arrays;

public class LC189 {
    public static void rotate(int[] nums, int k) {
        while (k > 0){
            int temp = nums[nums.length -1];
            for (int i = nums.length-1; i > 0;i--){
                nums[i] = nums[i-1];
            }
            nums[0] = temp;
            k--;
        }
    }

    public static void sol2(int[] nums, int k){
        k = k%nums.length;
        reverse(nums, 0, nums.length-1);
        reverse(nums, 0, k-1);
        reverse(nums, k, nums.length-1);
    }

    private static void reverse(int[] nums, int start, int end){
        while (start < end){
            int temp = nums[start];
            nums[start] = nums[end];
            nums[end] = temp;
            start++;
            end--;
        }
    }

    public static void main(String[] args){
        int[] t1= {1,2,3,4,5,6,7};
        int[] t2 = {-1,-100,3,99};
        //rotate(t1, 3);
        sol2(t1,3);
        System.out.println(Arrays.toString(t1));
        //rotate(t2,2);
        sol2(t2,2);
        System.out.println(Arrays.toString(t2));
    }
}
