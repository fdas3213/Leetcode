import java.util.List;
import java.util.ArrayList;

public class LC73 {
    public static void setZeroes(int[][] matrix) {
        int row = matrix.length, col = matrix[0].length;
        List<Integer> zero_r = new ArrayList<>();
        List<Integer> zero_c = new ArrayList<>();
        for(int i = 0; i < row; i++){
            for(int j = 0; j < col; j++){
                if(matrix[i][j] == 0) {
                    zero_r.add(i);
                    zero_c.add(j);
                }
            }
        }
        for(int i: zero_r) {
            for (int j = 0; j < col; j++) matrix[i][j] = 0;
        }
        for(int j : zero_c){
            for(int i = 0; i < row; i++) matrix[i][j] = 0;
        }
    }
    /*
    int col0 = 1, rows = matrix.size(), cols = matrix[0].size();

    for (int i = 0; i < rows; i++) {
        if (matrix[i][0] == 0) col0 = 0;
        for (int j = 1; j < cols; j++)
            if (matrix[i][j] == 0)
                matrix[i][0] = matrix[0][j] = 0;
    }

    for (int i = rows - 1; i >= 0; i--) {
        for (int j = cols - 1; j >= 1; j--)
            if (matrix[i][0] == 0 || matrix[0][j] == 0)
                matrix[i][j] = 0;
        if (col0 == 0) matrix[i][0] = 0;
    }
     */

    public static void main(String[] args){
        int[][] t1 = {{1,1,1},{1,0,1},{1,1,1}};
        int[][] t2 = {{0,1,2,0},{3,4,5,2},{1,3,1,5}};
        setZeroes(t1);
        Solution.print2dArray(t1);
        setZeroes(t2);
        Solution.print2dArray(t2);
    }
}
