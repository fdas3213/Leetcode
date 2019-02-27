import java.util.Arrays;

public class LC31 {
    private static void nextPermutation(int[] nums) {
        if (nums.length <= 1) return;
        int i = nums.length - 1;
        //find first number which is smaller than the number after
        for (; i >= 1; i--) {
            if (nums[i] > nums[i - 1]) break;
        }
        if (i != 0) swap(nums, i - 1); //if the number exist, it means that nums not like{5,4,3,2,1}
        reverse(nums, i);
    }

    private static void swap(int[] a,int i){
        for(int j = a.length-1;j>i;j--){
            if(a[j]>a[i]){
                int t = a[j];
                a[j] = a[i];
                a[i] = t;
                break;
            }
        }
    }

    private static void reverse(int[] a,int i){//reverse the number after the number we have found
        int first = i;
        int last = a.length-1;
        while(first<last){
            int t = a[first];
            a[first] = a[last];
            a[last] = t;
            first ++;
            last --;
        }
    }

    public static void main(String[] args){
        int[] t1 = {1,1,5};
        int[] t2 = {2,5,6,4,3};
        nextPermutation(t1);
        nextPermutation(t2);
        System.out.println(Arrays.toString(t1));
        System.out.println(Arrays.toString(t2));
    }
}
