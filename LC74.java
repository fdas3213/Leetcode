public class LC74 {
    public static boolean searchMatrix(int[][] matrix, int target) {
        if (matrix.length == 0 || matrix[0].length == 0) return false;
        int r = matrix.length, c = matrix[0].length;
        int begin = 0, end = r*c-1;
        while (begin<= end){
            int mid = (begin + end) / 2;
            int mid_val = matrix[mid/c][mid%c];
            if(target == mid_val) return true;
            else if(mid_val < target){
                begin = mid + 1;
            }else {
                end = mid - 1;
            }
        }
        return false;
    }

    public static void main(String[] args){
        int[][] t1 = {{1,3,5,7}, {10,11,16,20},{23,30,34,50}};
        System.out.println(searchMatrix(t1, 3));
    }
}
