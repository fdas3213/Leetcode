public class LC75 {
    public void sortColors(int[] nums) {
        //insertion sort
        int l = nums.length;
        for(int i = 1; i < l; i++){
            for (int j = i; j > 0 && nums[j]<nums[j-1]; j--){
                int tmp = nums[j];
                nums[j] = nums[j-1];
                nums[j-1] = tmp;
            }
        }
    }

    private void sortsol2(int[] nums){
        //in-place
        int n0 = 0, n1= 0, n2 =0;
        for (int i = 0; i < nums.length; i++){
            if(nums[i] == 0) ++n0;
            else if(nums[i] == 1) ++n1;
            else if(nums[i] == 2) ++n2;
        }

        for (int i = 0;i < n0; i++) nums[i] = 0;
        for (int i = 0; i<n1;i++) nums[i+n0] = 1;
        for (int i = 0;i<n2;i++) nums[i+n0+n1] = 2;
    }
}
