import java.util.ArrayList;
import java.util.List;

public class LC54 {
    private static List<Integer> spiralOrder(int[][] matrix) {
        List<Integer> out = new ArrayList<>();
        if (matrix.length == 0) return out;
        int rowbegin = 0, colbegin = 0;
        int rowEnd = matrix.length - 1, colEnd = matrix[0].length - 1;
        while (rowbegin <= rowEnd && colbegin <= colEnd){
            for(int i = colbegin; i <= colEnd; i++){
                //first add from left to right
                out.add(matrix[rowbegin][i]);
            }
            rowbegin++;
            for(int i = rowbegin; i <= rowEnd; i++){
                //then add from top to bottom
                out.add(matrix[i][colEnd]);
            }
            colEnd--;
            if(rowbegin <= rowEnd){
                //add from right to left
                for (int i = colEnd; i >= colbegin; i--){
                    out.add(matrix[rowEnd][i]);
                }
            }
            rowEnd--;
            if(colbegin <= colEnd){
                //add from bottom to top
                for (int i = rowEnd; i >= rowbegin; i--){
                    out.add(matrix[i][colbegin]);
                }
            }
            colbegin++;
        }
        return out;
    }

    public static void main(String[] args){
        int[][] t1 = {{1,2,3},{4,5,6},{7,8,9}};
        int[][] t2= {{1,2,3,4},{5,6,7,8},{9,10,11,12}};
        System.out.println(spiralOrder(t1));
        System.out.println(spiralOrder(t2));
    }
}
