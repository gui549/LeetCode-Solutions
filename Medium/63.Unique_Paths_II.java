package Medium;

import java.util.Arrays;

class Solution {

    static final int mod = 2 * 1000 * 1000 * 1000;

    public int uniquePathsWithObstacles(int[][] obstacleGrid) {
        if (obstacleGrid[0][0] == 1) {
            return 0;
        }
        
        int m = obstacleGrid.length, n = obstacleGrid[0].length;
        int [][] dp = new int[m][n];

        dp[0][0] = 1;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (obstacleGrid[i][j] != 1) {
                    if (i > 0) {
                        System.out.println(i + ", " + j);
                        dp[i][j] += dp[i - 1][j] % mod;
                    }

                    if (j > 0) {
                        System.out.println(i + ", " + j);
                        dp[i][j] += dp[i][j - 1] % mod;
                    }
                }
            }
        }
        for (int[] row : dp) {
            System.out.println(Arrays.toString(row));
        }
        return dp[m - 1][n - 1];
    }
}