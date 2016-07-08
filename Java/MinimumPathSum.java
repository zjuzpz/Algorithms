
public class MinimumPathSum {
    public int minPathSum(int[][] grid) {
        int m = grid.length;
        if(m == 0) {return 0;}
        int n = grid[0].length;
        int[] prev = grid[0].clone();
        for(int j = 1; j < n; j++) {
            prev[j] += prev[j - 1];
        }
        int[] cur = new int[n];
        for(int i = 1; i < m; i++) {
            cur[0] = prev[0] + grid[i][0];
            for(int j = 1; j < n; j++){
                cur[j] = grid[i][j] + Math.min(prev[j], cur[j - 1]);
            }
            prev = cur.clone();
        }
        return prev[n - 1];
    }

	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

}
