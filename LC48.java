import java.util.Arrays;

public class LC48 {
    public static void rotate(int[][] matrix) {
        //first matrix transpose, then flip left/right
        for (int i = 0; i < matrix.length; i++){
            for (int j = i; j < matrix.length;j++){
                int tmp = matrix[i][j];
                matrix[i][j] = matrix[j][i];
                matrix[j][i] = tmp;
            }
        }
        for (int i = 0; i < matrix.length; i++){
            for (int j = 0; j < matrix.length/2; j++){
                int tmp = matrix[i][j];
                matrix[i][j] = matrix[i][matrix.length-1-j];
                matrix[i][matrix.length-1-j] = tmp;
            }
        }
    }

    public static void main(String[] args){
        int[][] t1 = {{1,2,3},{4,5,6},{7,8,9}};
        int[][] t2 = {{5,1,9,11},{2,4,8,10},{13,3,6,7},{15,14,12,16}};

        rotate(t1);
        for (int i =0;i<t1.length;i++) System.out.println(Arrays.toString(t1[i]));
        rotate(t2);
        for (int i =0;i<t2.length;i++) System.out.println(Arrays.toString(t2[i]));

    }
}
