
public class DungeonGame {
    public int calculateMinimumHP(int[][] dungeon) {
        if(dungeon.length == 0) {return 1;}
        int m = dungeon.length;
        int n = dungeon[0].length;
        int[][] dp = new int[m][n];
        dp[m - 1][n - 1] = Math.max(0, -dungeon[m - 1][n - 1]);
        for(int i = m - 2; i >= 0; i--) {
            dp[i][n - 1] = Math.max(0, dp[i + 1][n - 1] - dungeon[i][n - 1]);
        }
        for(int j = n - 2; j >= 0; j--) {
            dp[m - 1][j] = Math.max(0, dp[m - 1][j + 1] - dungeon[m - 1][j]);
        }
        for(int i = m - 2; i >= 0; i--) {
            for(int j = n - 2; j >= 0; j--) {
                dp[i][j] = Math.max(0, Math.min(dp[i + 1][j], dp[i][j + 1]) - dungeon[i][j]);
            }
        }
        return dp[0][0] + 1;
    }

}
