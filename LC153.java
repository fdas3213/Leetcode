public class LC153 {
    public static int findMin(int[] nums){
        int low = 0, high = nums.length-1;
        while (low <= high){
            int mid = low + (high -low)/2;
            if (nums[high] > nums[low]) high = mid-1;
            else {
                if (nums[mid] > nums[low]) low = mid+1;
                else high = mid-1;
            }
        }
        return nums[low];
    }

    public static void main(String[] args){
        int[] t1 = {3,4,5,1,2};
        int[] t2 = {4,5,6,7,0,1,2};
        System.out.println(findMin(t1));
        System.out.println(findMin(t2));
    }
}
