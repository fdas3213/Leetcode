public class LC33 {
    public static int search(int[] nums, int target) {
        int start = 0, end = nums.length - 1;
        while (start <= end){
            int mid = (end + start)/2;
            if (nums[mid] == target) return mid;
            if(nums[start] <= nums[mid]) {
                if (target < nums[mid] && target >= nums[start]) end = mid - 1;
                else start = mid + 1;
            }
            if (nums[mid] <= nums[end]){
                if(target > nums[mid] && target <= nums[end]) start = mid + 1;
                else end = mid - 1;
            }
        }
        return -1;
    }

    public static void main(String[] args){
        int[] t1 = {4,5,6,7,0,1,2};
        System.out.println(search(t1,0));
        System.out.println(search(t1,3));
    }
}
