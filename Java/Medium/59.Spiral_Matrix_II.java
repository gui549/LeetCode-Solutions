package Medium;

class Solution {
    public int[][] generateMatrix(int n) {
        int[][] grid = new int[n][n];
        int count = 1;
        int up = 0, down = n - 1, left = 0, right = n - 1;
        while (count <= n * n) {
            for (int j = left; j <= right && count <= n * n; j++) {
                grid[up][j] = count++;
            }

            for (int i = up + 1; i <= down - 1 && count <= n * n; i++) {
                grid[i][right] = count++;
            }

            for (int j = right; j >= left && count <= n * n; j--) {
                grid[down][j] = count++;
            }

            for (int i = down - 1; i >= up + 1 && count <= n * n; i--) {
                grid[i][left] = count++;
            }

            up++; down--; left++; right--;
        }
        return grid;
    } 
}