package Easy;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;


class Solution {
    public List<List<Integer>> shiftGrid(int[][] grid, int k) {
        List<List<Integer>> ans = new ArrayList<>();
        int m = grid.length, n = grid[0].length;
        k %= m * n;

        reverse(grid, 0, m * n - 1);
        reverse(grid, 0, k - 1);
        reverse(grid, k, m * n - 1);
        
        for (int[] row : grid)
            ans.add(Arrays.stream(row).boxed().collect(Collectors.toList()));

        return ans;
    }

    private void reverse(int[][] grid, int lo, int hi) {
        int m = grid.length, n = grid[0].length;
        while (lo < hi) {
            int r1 = lo / n, c1 = lo % n, r2 = hi / n, c2 = hi % n;
            int tmp = grid[r1][c1];
            grid[r1][c1] = grid[r2][c2];
            grid[r2][c2] = tmp;
            lo++; hi--;
        }

    }
}


/*
class Solution {
    public List<List<Integer>> shiftGrid(int[][] grid, int k) {
        List<List<Integer>> ans = new ArrayList<>();
        int m = grid.length, n = grid[0].length;
        k %= m * n;

        for (int i = 0; i < k; i++) {
            step(grid);
        }
        
        for (int[] row : grid) {
            ans.add(Arrays.stream(row).boxed().collect(Collectors.toList()));
        }

        return ans;
    }

    private void step(int[][] grid) {
        int m = grid.length, n = grid[0].length;
        int temp1 = grid[m - 1][n - 1], temp2;
        for (int i = 0; i < m; i++) {
            temp2 = grid[i][n - 1];
            for (int j = n - 1; j > 0; j--) {
                grid[i][j] = grid[i][j - 1];
            }
            grid[i][0] = temp1;
            temp1 = temp2;
        }
    }
}
*/