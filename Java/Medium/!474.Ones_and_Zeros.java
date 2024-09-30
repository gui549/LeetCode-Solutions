package Medium;


class Solution {
    public int findMaxForm(String[] strs, int m, int n) {
        int[][] dp = new int[m + 1][n + 1];
        for (String s : strs) {
            int zeros = (int) s.chars().filter(ch -> (ch == '0')).count();
            int ones = s.length() - zeros;

            for (int i = m; i >= zeros; i--) {
                for (int j = n; j >= ones; j--) {
                    dp[i][j] = Math.max(1 + dp[i - zeros][j - ones], dp[i][j]);
                }
            }
        }

        return dp[m][n];
    }
}