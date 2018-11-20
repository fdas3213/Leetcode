import java.lang.Math;

public class LC11 {
    public static int maxArea(int[] height){
        //brute force way
        int max = 0;
        for (int i =0; i < height.length; i++){
            for (int j = i+1; j<height.length; j++){
                int area = (j-i) * Math.min(height[i], height[j]);
                if (max < area) max = area;
            }
        }
        return max;
    }

    public static int maxAreafast(int[] height){
        int i = 0;
        int j = height.length-1;
        int water = 0;
        while (i < j){
            water = Math.max(water, (j-i)*Math.min(height[i], height[j]));
            if (height[i] < height[j]) i++;
            else j--;
        }
        return water;
    }

    public static void main(String[] args){
        //unit test 1
        int[] arr1 = {1,8,6,2,5,4,8,3,7};
        System.out.println(maxArea(arr1));
        System.out.println(maxAreafast(arr1));
    }
}
