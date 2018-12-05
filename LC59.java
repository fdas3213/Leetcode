import java.util.Arrays;

public class LC59 {
    public static int[][] generateMatrix(int n){
        int[][] out = new int[n][n];
        int rowStart = 0, colStart = 0;
        int rowEnd = n-1, colEnd = n-1;
        int val = 1;
        while(rowStart <= rowEnd && colStart <= colEnd){
            for(int i = colStart;i <= colEnd; i++){
                //fill in from left to right
                out[rowStart][i] = val++;
            }
            rowStart++;
            for(int i = rowStart; i<= rowEnd; i++){
                //fill in from top to bottom
                out[i][colEnd] = val++;
            }
            colEnd--;
            if(rowStart <= rowEnd){
                for (int i = colEnd; i>= colStart; i--){
                    //fill in from right to left
                    out[rowEnd][i] = val++;
                }
            }
            rowEnd--;
            if(colStart <= colEnd){
                for(int i = rowEnd; i >= rowStart; i--){
                    //fill in from bottom to top
                    out[i][colStart] = val++;
                }
            }
            colStart++;
        }
        return out;
    }
    public static void main(String[] args){
        int[][] output = generateMatrix(3);
        for (int i = 0; i< 3; i++){
            System.out.println(Arrays.toString(output[i]));
        }
    }
}
