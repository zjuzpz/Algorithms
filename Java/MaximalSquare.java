
public class MaximalSquare {
    public int maximalSquare(char[][] matrix) {
        int m = matrix.length;
        if(m == 0) {return 0;}
        int n = matrix[0].length;
        int res = 0;
        int[][] lookup = new int[m][n];
        for(int i = 0; i < m ;i++) {
            if(matrix[i][0] == '1') {
                res = 1;
                lookup[i][0] = 1;
            }
        }
        for(int j = 0; j < n; j++) {
            if(matrix[0][j] == '1') {
                res = 1;
                lookup[0][j] = 1;
            }
        }
        for(int i = 1; i < m; i++) {
            for(int j = 1; j < n; j++) {
                if(matrix[i][j] == '1') {
                    lookup[i][j] = Math.min(lookup[i - 1][j - 1], Math.min(lookup[i - 1][j], lookup[i][j - 1])) + 1;
                    res = Math.max(res, lookup[i][j]);
                }
            }
        }
        return res * res;
    }

}
