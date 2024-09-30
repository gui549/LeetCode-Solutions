package Medium;

class Solution {
    public int uniquePaths(int m, int n) {
        final int mod = 2000000000;
        int[][] dp = new int[m][n];
        dp[0][0] = 1;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (0 < i) dp[i][j] = dp[i][j] + dp[i - 1][j] % mod;
                if (0 < j) dp[i][j] = dp[i][j] + dp[i][j - 1] % mod;
            }
        }
        return dp[m - 1][n - 1];
    }
}