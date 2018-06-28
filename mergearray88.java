public class mergearray88 {
    public static void main(String[] args){
        int[] l1 = {1,2,3,0,0,0};
        int[] l2 = {2,5,6};
    }

    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int l1 = 0;
        int l2 = 0;
        while (l1 < m + n && l2 < n){
            //need to move every element one position back
            if (nums1[l1] > nums2[l2]){
                for (int i = l1;i < m +n;i++){
                    nums1[i+1] = nums1[i];
                }
            }
        }
    }
}
