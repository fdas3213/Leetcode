import java.util.Arrays;

public class LC34 {
    public static int[] searchRange(int[] nums, int target) {
        int start = 0,  end = nums.length-1;
        int[] out = {-1,-1};
        int idx = -1;
        while (start <= end){
            int mid = (start + end)/2;
            if (nums[mid] < target) start = mid+1;
            else if (nums[mid] > target) end = mid-1;
            else {
                idx = mid;
                break;
            }
        }
        if (idx != -1){
            int firstpos = idx, lastpos = idx;
            while(firstpos > 0 && nums[firstpos] == nums[firstpos-1]) firstpos --;
            while(lastpos < nums.length - 1 && nums[lastpos] == nums[lastpos+1]) lastpos ++;
            out[0] = firstpos;
            out[1] = lastpos;
        }
        return out;
    }
    

    public static void main(String[] args){
        int[] t = {5,7,7,8,8,10};
        System.out.println(Arrays.toString(searchRange(t, 8)));
    }
}
