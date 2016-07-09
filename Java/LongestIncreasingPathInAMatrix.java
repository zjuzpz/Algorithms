
public class LongestIncreasingPathInAMatrix {
    public int longestIncreasingPath(int[][] matrix) {
        if(matrix.length == 0) {return 0;}
        int m = matrix.length;
        int n = matrix[0].length;
        int[][] path = new int[m][n];
        int res = 1;
        for(int i = 0; i < m; i++) {
            for(int j = 0; j < n; j++) {
                if(path[i][j] == 0) {
                    res = Math.max(res, DFS(path, matrix, i, j));
                } 
            }
        }
        return res;
    }
    
    public int DFS(int[][] path, int[][] matrix, int i, int j) {
        if(path[i][j] != 0) {
            return path[i][j];
        }
        int res = 0;
        int[][] directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        for(int[] direction: directions) {
            int x = i + direction[0];
            int y = j + direction[1];
            if(x >= 0 && x < path.length && y >= 0 && y < path[0].length) {
                if(matrix[x][y] < matrix[i][j]) {
                    res = Math.max(res, DFS(path, matrix, x, y));
                }
            }
        }
        path[i][j] = res + 1;
        return path[i][j];
    }

}
