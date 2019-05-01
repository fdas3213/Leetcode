import java.util.Arrays;
import java.util.LinkedList;

public class LC130 {
    public static void solve(char[][] board) {
        //using BFS
        if (board == null || board.length == 0) return;
        int n = board.length, m = board[0].length;
        //use a queue to store coordinates of edge 'O's
        LinkedList<String> q = new LinkedList<>();
        //first find all O's on the edge
        for (int i = 0; i <n;i++){
            if (board[i][0] == 'O') {
                board[i][0] = '+';
                q.add(String.valueOf(i) + ','+'0');

            }
            if (board[i][m-1] == 'O') {
                board[i][m-1] = '+';
                q.add(String.valueOf(i)+','+ (m-1));
            }
        }
        for (int j = 0; j < m; j++){
            if (board[0][j] == 'O') {
                board[0][j] = '+';
                q.add(String.valueOf('0') +','+ (j));
            }
            if (board[n-1][j] == 'O') {
                board[n-1][j] = '+';
                q.add(String.valueOf(n-1)+',' +(j));
            }
        }
        //using bfs to find all 'O's that connect to '0's on the border
        while (!q.isEmpty()){
            String coor = q.poll();
            int i = Integer.parseInt(coor.substring(0, coor.indexOf(",")));
            int j = Integer.parseInt(coor.substring(coor.indexOf(",")+1));
            if(i+1 <n && board[i+1][j] == 'O') {
                board[i+1][j] = '+';
                q.add(String.valueOf(i+1)+','+j);
            }
            if(i-1 >= 0 && board[i-1][j] == 'O') {
                board[i-1][j] = '+';
                q.add(String.valueOf(i-1)+','+j);
            }
            if(j+1 < m && board[i][j+1] == 'O'){
                board[i][j+1] = '+';
                q.add(String.valueOf(i)+','+(j+1));
            }
            if(j-1 >= 0 && board[i][j-1] == 'O'){
                board[i][j-1] = '+';
                q.add(String.valueOf(i)+',' +(j-1));
            }
        }
        //transform 'O' to 'X', and '+' to 'O'
        for(int i = 0; i< n; i++){
            for (int j = 0; j<m; j++){
                if(board[i][j] == 'O') board[i][j] = 'X';
                else if (board[i][j] == '+') board[i][j] = 'O';
            }
        }
    }

    public static void main(String[] args){
        char[][] c1 = {{'X','X','X','X'},{'X','O','O','X'},{'X','X','O','X'},
                {'X','O','X','X'}};
        for (int i = 0; i < c1.length; i++){
            System.out.println(Arrays.toString(c1[i]));
        }
        solve(c1);
        for (int i = 0; i < c1.length; i++){
            System.out.println(Arrays.toString(c1[i]));
        }
    }
}
