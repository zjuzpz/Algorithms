
public class BurstBalloons {
    public int maxCoins(int[] nums) {
        if(nums == null || nums.length == 0) {return 0;}
        int[] coins = new int[nums.length + 2];
        coins[0] = 1;
        coins[coins.length - 1] = 1;
        for(int i = 0; i < nums.length; i++) {
            coins[i + 1] = nums[i];
        }
        int[][] dp = new int[coins.length][coins.length];
        for(int i = coins.length - 2; i >= 1; i--) {
            dp[i][i] = coins[i - 1] * coins[i] * coins[i + 1];
            for(int j = i + 1; j < coins.length - 1; j++) {
                dp[i][j] = Math.max(dp[i + 1][j] + coins[i - 1] * coins[i] * coins[j + 1], dp[i][j - 1] + coins[i - 1] * coins[j] * coins[j + 1]);
                for(int k = i + 1; k <= j - 1; k++) {
                    dp[i][j] = Math.max(dp[i][j], dp[i][k - 1] + dp[k + 1][j] + coins[i - 1] * coins[k] * coins[j + 1]);
                }
            }
        }
        return dp[1][dp.length - 2];
    }

}
