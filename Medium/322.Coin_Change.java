package Medium;

import java.util.Arrays;

class Solution {
    public int coinChange(int[] coins, int amount) {
        if (amount == 0) {
            return 0;
        }
        
        int[] dp = new int[amount + 1];
        Arrays.fill(dp, Integer.MAX_VALUE);        
        dp[0] = 0;

        for (int i = 0; i < amount + 1; i++) {
            if (dp[i] == Integer.MAX_VALUE) {
                continue;
            }

            for (int coin : coins) {
                if (0 < i + coin && i + coin < amount + 1) {
                    dp[i + coin] = Math.min(dp[i + coin], dp[i] + 1);
                }
            }
        }

        return dp[amount] == Integer.MAX_VALUE ? -1 : dp[amount];
    }
}