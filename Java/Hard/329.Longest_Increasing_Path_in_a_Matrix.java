package Hard;

class Solution {
    
    int[][] movements = new int[][]{{0,1}, {0,-1}, {1,0}, {-1,0}};
    
    public int longestIncreasingPath(int[][] matrix) {
        int m = matrix.length, n = matrix[0].length;
        int[][] dp = new int[m][n];

        int ans = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (dp[i][j] == 0) {
                    dp[i][j] = dfs(matrix, dp, i, j);
                    ans = Math.max(ans, dp[i][j]);
                }
            }
        }

        return ans;
    }

    private int dfs(int[][] matrix, int[][] dp, int r, int c) {
        int m = matrix.length, n = matrix[0].length, res = 1;

        for (int[] movement : movements) {
            int nr = r + movement[0];
            int nc = c + movement[1];

            if (0 <= nr && nr < m && 0 <= nc && nc < n && matrix[r][c] < matrix[nr][nc]) {
                if (dp[nr][nc] != 0) {
                    res = Math.max(res, dp[nr][nc] + 1);
                } else {
                    res = Math.max(res, dfs(matrix, dp, nr, nc) + 1);
                }
            }
        }

        dp[r][c] = res;
        return dp[r][c];
    }
}