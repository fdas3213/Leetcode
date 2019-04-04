import java.util.HashSet;

public class LC36 {
    private static boolean isValidSudoku(char[][] board){
        for (int i = 0; i < board.length; i ++) {
            HashSet<Character> row = new HashSet<>();
            HashSet<Character> col = new HashSet<>();
            HashSet<Character> square = new HashSet<>();
            for (int j = 0; j < board.length; j++){
                //check each row
                if (board[i][j] != '.' && !row.add(board[i][j])) return false;
                //check for each col
                if (board[j][i] != '.' && !col.add(board[j][i])) return false;
                //check for 3*3 square
                int ridx = 3 * (i/3);
                int cidx = 3 * (i%3);
                if(board[ridx + j/3][cidx+j%3] != '.' && !square.add(board[ridx+j/3][cidx+j%3])) return false;
            }
        }
        return true;
    }

    private static boolean easyValidSudoku(char[][] board){
        HashSet<String> out = new HashSet<>();
        for (int i = 0; i < board.length; i++){
            for (int j = 0; j <board[i].length; j++){
                char number = board[i][j];
                if (number != '.'){
                    if(!out.add(number + "row" + i) || !out.add(number + "col" +j)||
                            !out.add(number + "square" +i/3+j/3)) return false;
                }
            }
        }
        return true;
    }

    public static void main(String[] args){
        HashSet<Integer> test = new HashSet<>();
        for(int i = 0;i < 9;i++){
            for (int j = 0;j<9;j++){
                int ridx = 3 * (i/3);
                int cidx = 3 * (i%3);
                System.out.println("i: "+i + " j: "+j + " ridx:" + ridx +" cidx: "+cidx +
                        " ridx + j/3: " + (ridx+j/3) + " cidx+j%3: " + (cidx+j%3));
            }
        }
    }
}
