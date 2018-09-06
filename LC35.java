public class LC35 {
    public static int searchInsert(int[] nums, int target) {
        if (target <= nums[0]) return 0;
        for (int i = 1; i < nums.length; i++){
            if (target <= nums[i] && target > nums[i-1]) return i;
        }
        return nums.length;
    }

    public static int binarysearchInsert(int[] nums, int target){
        int low = 0, high = nums.length-1;
        while(low <= high){
            int mid = low + (high-low)/2;
            if(nums[mid] == target) return mid;
            else if(nums[mid] > target) high = mid -1;
            else low = mid+1;
        }
        return low;
    }

    public static void main(String[] args){
        int[] arr1 = {1,3,5,6};
        System.out.println(searchInsert(arr1,6));
        System.out.println(searchInsert(arr1,3));
        System.out.println(searchInsert(arr1,1));
        System.out.println(searchInsert(arr1,5));
    }
}
