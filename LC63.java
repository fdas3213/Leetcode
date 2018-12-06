public class LC63 {
    private static int uniquePathsWithObstacles(int[][] obstacleGrid){
        if(obstacleGrid[0][0] == 1) return 0;
        int m = obstacleGrid.length, n = obstacleGrid[0].length;
        int[][] dp = new int[m][n];
        dp[0][0] = 1;
        for(int i = 1; i < m; i++){
            if (obstacleGrid[i][0] != 1) dp[i][0] = 1;
            else{
                for (int j = i; j < m; j++) dp[j][0] = 0;
                break;
            }
        }
        for(int j = 1; j < n; j++){
            if(obstacleGrid[0][j] != 1) dp[0][j] = 1;
            else{
                for (int i = j; i < n; i++) dp[0][i] = 0;
                break;
            }
        }
        for (int i = 1; i < m; i++){
            for (int j = 1; j < n; j++){
                if(obstacleGrid[i][j] != 1) dp[i][j] = dp[i-1][j] + dp[i][j-1];
                else dp[i][j] = 0;
            }
        }
        return dp[m-1][n-1];

    }
    public static void main(String[] args){
        int[][] t1 = {{0,0,0},{0,1,0},{0,0,0}};
        System.out.println(uniquePathsWithObstacles(t1));
        int[][] t2 = {{0}};
        System.out.println(uniquePathsWithObstacles(t2));

    }
}
