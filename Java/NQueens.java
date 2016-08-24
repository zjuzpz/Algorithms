import java.util.*;
public class NQueens {
    public List<List<String>> solveNQueens(int n) {
        List<List<String>> res = new ArrayList<List<String>>();
        if(n <= 0) {return res;}
        char[][] board = new char[n][n];
        for(int i = 0; i < n; i++) {
            Arrays.fill(board[i], '.');
        }
        helper(res, board, 0, n);
        return res;
    }
    
    private void helper(List<List<String>> res, char[][] board, int x, int n) {
        if(x == n) {
            List<String> cur = new ArrayList<String>();
            StringBuffer row;
            for(int i = 0; i < n; i++) {
                row = new StringBuffer();
                for(int j = 0; j < n; j++) {
                    row.append(board[i][j]);
                }
                cur.add(row.toString());
            }
            res.add(cur);
        } else {
            for(int j = 0; j < n; j++) {
                board[x][j] = 'Q';
                if(isValid(board, x, j)) {
                    helper(res, board, x + 1, n);
                }
                board[x][j] = '.';
            }
        }
    }
    
    private boolean isValid(char[][] board, int x, int y) {
        for(int i = 0; i < x; i++) {
            if(board[i][y] == 'Q'){
                return false;
            }
        }
        int i = x - 1;
        int j = y - 1;
        while(i >= 0 && j >= 0) {
            if(board[i][j] == 'Q') {
                return false;
            }
            i--;
            j--;
        }
        i = x - 1;
        j = y + 1;
        while(i >= 0 && j < board.length) {
            if(board[i][j] == 'Q') {
                return false;
            }
            i--;
            j++;
        }
        return true;
    }

}
