public class insertposition36 {
    public static void main(String[] args){
        int[] l1 = {1,3,5,6};
        System.out.println(searchInsert(l1,5));
        System.out.println(searchInsert(l1,2));
        System.out.println(searchInsert(l1,0));
        System.out.println(searchInsert(l1,7));
    }

    public static int searchInsert(int[] nums, int target){
        if (nums.length == 0) return 0;
        for (int i = 0; i< nums.length; i ++){
            if (nums[i] >= target) return i;
        }
        return nums.length;
    }
}
