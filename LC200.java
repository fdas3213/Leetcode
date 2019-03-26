
public class LC200 {
    public static int numIslands(char[][] grid) {
        if (grid == null || grid.length == 0) return 0;
        int n =grid.length, m = grid[0].length;
        int count = 0;
        for (int i = 0; i< n; i++){
            for (int j = 0; j < m; j++){
                if (grid[i][j] == '1'){
                    count ++;
                    DFS(grid, i, j);
                }
            }
        }
        return count;
    }

    private static void DFS(char[][] grid, int i, int j){
        if (i < 0 || j < 0 || i >= grid.length || j >= grid[0].length || grid[i][j] != '1') return;
        grid[i][j] = '0';
        DFS(grid, i+1, j);
        DFS(grid,i-1,j);
        DFS(grid, i, j+1);
        DFS(grid, i, j-1);
    }

    public static void main(String[] args){
        char[][] c1 = {{'1','1','0','0','0'}, {'1','1','0','0','0'},
                {'0','0','1','0','0'},{'0','0','0','1','1'}};
        System.out.println(numIslands(c1));
    }
}
