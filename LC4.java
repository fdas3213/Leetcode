public class LC4 {
    public static double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int x = nums1.length, y = nums2.length;
        if (x > y) return findMedianSortedArrays(nums2, nums1);
        int left = 0, right = x;
        while (left <= right){
            int partitionX = left + (right-left)/2;
            int partitionY = (x+y+1)/2 - partitionX;
            /*edge case where left or right partition is empty */
            int maxLeftX = (partitionX==0) ? Integer.MIN_VALUE : nums1[partitionX-1];
            int minRightX = (partitionX==x) ? Integer.MAX_VALUE : nums1[partitionX];
            int maxLeftY = (partitionY==0) ? Integer.MIN_VALUE : nums2[partitionY-1];
            int minRightY = (partitionY==y) ? Integer.MAX_VALUE : nums2[partitionY];

            if (maxLeftX <= minRightY && maxLeftY <= minRightX){
                if ((x+y)%2 == 0) {
                    return ((double)Math.max(maxLeftX, maxLeftY) + Math.min(minRightX, minRightY)) /2;
                }else{
                    return (double) Math.max(maxLeftX, maxLeftY);
                }
            }else if (maxLeftX > minRightY) right = partitionX-1;
            else left = partitionX+1;
        }
        return -1;
    }

    public double BruteForceSol(int[] nums1, int[] nums2){
        int total = nums1.length+nums2.length;
        double[] res = new double[total];
        int i =0, j=0;
        for (int k = 0; k<total;k++){
            if (i == nums1.length) res[k] = (double)nums2[j++];
            else if (j == nums2.length) res[k] = (double)nums1[i++];
            else if (nums1[i] <= nums2[j]) res[k] = (double)nums1[i++];
            else res[k] = (double)nums2[j++];
        }
        return total%2!=0 ? res[total/2] : (res[total/2] + res[total/2 -1])/2;
    }

    public static void main(String[] args){
        int[] l1 = {1,3};
        int[] l2 = {2};
        System.out.println(findMedianSortedArrays(l1,l2));
        int[] l3 = {1,2};
        int[] l4 = {3,4};
        System.out.println(findMedianSortedArrays(l3,l4));
    }
}
