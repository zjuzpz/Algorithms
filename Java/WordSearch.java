
public class WordSearch {
    public boolean exist(char[][] board, String word) {
        if(word.length() == 0) {return true;}
        int m = board.length;
        if(m == 0) {return false;}
        int n = board[0].length;
        boolean[][] visited = new boolean[m][n];
        for(int i = 0; i < m; i++) {
            for(int j = 0; j < n; j++) {
                if(board[i][j] == word.charAt(0)) {
                    visited[i][j] = true;
                    if(DFS(board, i, j, visited, word, 1)) {return true;}
                    visited[i][j] = false;
                }
            }
        }
        return false;
    }
    
    private boolean DFS(char[][] board, int x, int y, boolean[][] visited, String word, int start) {
        if(start == word.length()) {return true;}
        int[][] directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        int i;
        int j;
        for(int[] direction: directions) {
            i = x + direction[0];
            j = y + direction[1];
            if(i >= 0 && i < visited.length && j >= 0 && j < visited[0].length && !visited[i][j] && board[i][j] == word.charAt(start)) {
                visited[i][j] = true;
                if(DFS(board, i, j, visited, word, start + 1)) {return true;}
                visited[i][j] = false;
            }
        }
        return false;
    }

}
