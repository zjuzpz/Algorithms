
public class GuessNumberHigherOrLowerII {
    public int getMoneyAmount(int n) {
        if(n == 1) {return 0;}
        int[][] dp = new int[n + 1][n + 1];
        for(int i = n - 1; i >= 1; i--) {
            for(int j = i + 1; j <= n; j++) {
                dp[i][j] = Integer.MAX_VALUE;
                for(int k = i; k < j; k++) {
                    dp[i][j] = Math.min(dp[i][j], k + Math.max(dp[i][k - 1], dp[k + 1][j]));
                }
            }
        }
        return dp[1][n];
    }

	public static void main(String[] args) {
		for(int i = 1; i < 5; i++) {
			System.out.println(new GuessNumberHigherOrLowerII().getMoneyAmount(i));
		}

	}

}
