public class LC64 {
    private static int minPathSum(int[][] grid){
        int row = grid.length, column = grid[0].length;
        int[][] dp = new int[row][column];
        dp[0][0] = grid[0][0];
        for (int i = 1; i < row; i++) {
            //fill out the values of each row, first column
            dp[i][0] = dp[i-1][0] + grid[i][0];
        }
        for (int j = 1; j <column; j++){
            //fill out the values of each column, first row
            dp[0][j] = dp[0][j-1] + grid[0][j];
        }
        for (int i = 1; i < row; i++){
            for (int j = 1; j < column; j++){
                dp[i][j] = Math.min(dp[i-1][j], dp[i][j-1]) + grid[i][j];
            }
        }
        return dp[row-1][column-1];
    }

    private static int anotherone(int[][] grid){
        //put everything in one loop and use no extra space
        int row = grid.length, column = grid[0].length;
        for (int i = 0; i < row; i++){
            for (int j = 0; j < column; j++){
                if(i == 0 && j == 0) continue;
                else if (i == 0 && j != 0) grid[i][j] += grid[i][j-1];
                else if (i != 0 && j == 0) grid[i][j] += grid[i-1][j];
                else grid[i][j] += Math.min(grid[i][j-1], grid[i-1][j]);
            }
        }
        return grid[row-1][column-1];
    }


    public static void main(String[] args){
        int[][] test1 = {{1,3,1},{1,5,1},{4,2,1}};
        int[][] test2 = {{1,2},{5,6},{1,1}};
        System.out.println(minPathSum(test1));
        System.out.println(minPathSum(test2));
    }
}
