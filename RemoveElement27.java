import java.util.Arrays;

public class RemoveElement27 {

    public static void main(String[] args){
        int[] t1 = {3,2,2,3};
        int[] t2 = {0,1,2,2,3,0,4,2};
        System.out.println(Arrays.toString(removeElement(t1,3)));
        System.out.println(Arrays.toString(removeElement(t2,2)));
    }


    public static int[] removeElement(int[] nums, int val) {
        if (nums.length == 0) return nums;
        int len = 0;
        int i = 0, j = 0;
        while (i < nums.length){
            if (nums[i] == val){
                j = i;
                while((nums[j] == nums[i]) && (j < nums.length)){
                    j ++;
                }
                System.out.println("j: " + j + " i: " + i);
                nums[i] = nums[j];
                len ++;
            }
            i ++;
        }
        return nums;
    }


}
