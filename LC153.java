public class LC153 {
    public static int findMin(int[] nums){
        int low = 0, high = nums.length-1;
        while (low < high){
            int mid = low + (high -low)/2;
            if (nums[mid] < nums[high]) high = mid;
            else if (nums[mid] > nums[high]) low = mid+1;
        }
        return nums[low];
    }

    private static int Sol2(int[] nums){
        /*
        2 conditions:
        (a) if rotated: if mid > 0 and nums[mid] < nums[mid-1], then return nums[mid]
        (b) if not rotated: nums[0]
         */
        int low = 0, high = nums.length-1;
        while(low < high){
            int mid = low + (high - low)/2;
            if(mid > 0 && nums[mid] < nums[mid-1]) return nums[mid];
            //if mid element is greater than both ends, then search right hand side
            if(nums[mid] >= nums[low] && nums[mid] > nums[high]) low = mid+1;
            //else search left hand side
            else high = mid-1;
        }
        return nums[low];
    }

    public static void main(String[] args){
        int[] t1 = {3,4,5,1,2};
        int[] t2 = {4,5,6,7,0,1,2};
        int[] t3 = {3,1,2};
        System.out.println(findMin(t1));
        System.out.println(findMin(t2));
        System.out.println(findMin(t3));
    }
}
