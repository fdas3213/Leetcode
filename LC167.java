/*
Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

Note:

Your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you may not use the same element twice.
Example:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
 */
import java.util.Arrays;
import java.util.HashMap;

public class LC167 {
    public static int[] twoSum(int[] numbers, int target) {
        int[] solution = new int[2];
        HashMap<Integer, Integer> sol = new HashMap<>();
        for (int i = 0; i < numbers.length;i++){
            if (!sol.containsKey(numbers[i])) sol.put(target-numbers[i], i+1);
            else{
                solution[0] = sol.get(numbers[i]);
                solution[1] = i+1;
                break;
            }
        }
        return solution;
    }

    public static int[] twoSumSol2(int[] numbers, int target){
        int start = 0, end = numbers.length-1;
        while (start < end){
            if (numbers[start] + numbers[end] == target) break;
            else if(numbers[start] + numbers[end] > target) end--;
            else start++;
        }
        return new int[]{start+1, end+1};
    }

    public static void main(String[] args){
        int[] t1 = {2,7,11,15};
        System.out.println(Arrays.toString(twoSum(t1,9)));
        System.out.println(Arrays.toString(twoSumSol2(t1, 9)));
    }
}
