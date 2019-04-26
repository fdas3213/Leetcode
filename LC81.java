public class LC81 {
    public static boolean search(int[] nums, int target){
        int start = 0, end = nums.length -1;
        while (start <= end){
            int mid = start + (end - start)/2;
            if (nums[mid] == target) return true;
            while (start < mid && nums[start] == nums[mid]) start++;
            if (nums[start] <= nums[mid]){
                if(target >= nums[start] && target < nums[mid]) end = mid - 1;
                else start = mid + 1;
            }
            else{
                if(target > nums[mid] && target <= nums[end]) start = mid + 1;
                else end = mid - 1;
            }
        }
        return false;
    }

    public static void main(String[] args){
        int[] t1 = {2,5,6,0,0,1,2};
        System.out.println(search(t1,0));
        System.out.println(search(t1,3));
        int[] t2 = {1,1,3,1};
        System.out.println(search(t2,3));
    }
}
