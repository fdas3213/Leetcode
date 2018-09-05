import java.util.Arrays;

public class LC27 {
    public static int removeElement(int[] nums, int val) {
        int total = 0;
        for (int i = 0; i < nums.length; i++){
            if (nums[i] == val){
                for (int j = i; j < nums.length; j++){
                    if (nums[j] != nums[i]){
                        int temp = nums[i];
                        nums[i] = nums[j];
                        nums[j] = temp;
                        break;
                    }
                }
            }
        }
        for (int n :nums){
            if (n != val) total++;
        }
        return total;
    }

    public static int removeElementFast(int[] nums, int val){
        int start = 0;
        for(int i = 0; i<nums.length;i++){
            if (nums[i] != val){
                nums[start++] = nums[i];
            }
        }
        return start;
    }



    public static void main(String[] args){
        int[] t1 = {0,1,2,2,3,0,4,2};
        System.out.println(removeElement(t1,2));
        System.out.println(removeElementFast(t1, 2));
        int[] t2 = {3,2,2,3};
        System.out.println(removeElement(t2,3));
        System.out.println(removeElementFast(t2,3));
    }
}
