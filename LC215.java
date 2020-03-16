import java.util.Random;

public class LC215 {
    public static int findKthLargest(int[] nums, int k) {
        int n = nums.length;
        int low = 0, high = n-1;
        Random rand = new Random(0);

        while(low <= high){
            int pivotIndex = rand.nextInt(high-low+1)+low;
            int pivotValIndex = Partition(nums, pivotIndex, low, high);
            if (pivotValIndex == n-k) return nums[n-k];
            else if (pivotValIndex > n-k) high = pivotValIndex-1;
            else low = pivotValIndex+1;
        }
        return -1;
    }

    private static int Partition(int[] arr, int pivotIdx, int low, int high){
        int pivotVal = arr[pivotIdx];
        int finalpivotIndex = low;
        swap(arr, pivotIdx, high);
        for (int j = low; j < high; j++){
            if (arr[j] < pivotVal){
                swap(arr, finalpivotIndex++, j);
            }
        }
        swap(arr, finalpivotIndex, high);
        return finalpivotIndex;
    }

    private static void swap(int[] arr, int i, int j){
        int tmp = arr[i];
        arr[i] = arr[j];
        arr[j] = tmp;
    }

    public static void main(String[] args){
        int[] t1 = {3,2,1,5,6,4};
        System.out.println(findKthLargest(t1,2));
        int[] t2 = {3,2,3,1,2,4,5,5,6};
        System.out.println(findKthLargest(t2,4));
    }
}
