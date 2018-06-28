import java.util.Arrays;

public class mergesorted88 {
    public static void merge(int[] nums1, int m, int[] nums2, int n) {
        if (n == 0 || m == 0) return;
        int i = 0;
        int j = 0;
        while (i < nums1.length) {
            if (nums1[i] >= nums2[j]) {
                for (int k = (m - 1); k >= i; k--) {
                    nums1[k + 1] = nums1[k];
                }
                m++;
                j++;
            }else if (nums1[i] < nums2[j] && nums1[i] == 0){
                nums1[i] = nums2[j++];
            }
            i++;
        }
    }
    public static void main(String[] args){
        int[] l1 = {1,2,3,0,0,0};
        int[] l2 = {2,5,6};
        merge(l1, 3, l2,3);
        System.out.println(Arrays.toString(l1));

        int[] t1 = {2,0};
        int[] t2 = {1};
        merge(t1,1, t2, 1);
        System.out.println(Arrays.toString(t1));
    }
}
