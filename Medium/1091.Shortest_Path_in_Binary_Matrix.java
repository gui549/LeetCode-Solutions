package Medium;

import java.util.LinkedList;
import java.util.Queue;


class Solution {

    static final int[][] movements = new int[][]{{0, 1}, {0, -1}, {1, 0}, {-1, 0}, {1, 1}, {1, -1}, {-1, 1}, {-1, -1}};

    public int shortestPathBinaryMatrix(int[][] grid) {
        int m = grid.length, n = grid[0].length;
        if (grid[0][0] != 0 || grid[m - 1][n - 1] != 0) {
            return -1;
        }

        boolean[][] visited = new boolean[m][n];
        Queue<int[]> queue = new LinkedList<>();
        queue.add(new int[]{0, 0});
        visited[0][0] = true;
        int ans = 1;
        while (!queue.isEmpty()) {
            int size = queue.size();
            for (int i = 0; i < size; i++) {
                int[] element = queue.poll();
                if (element[0] == m - 1 && element[1] == n - 1) {
                    return ans;
                }
                for (int[] movement : movements) {
                    int nr = element[0] + movement[0];
                    int nc = element[1] + movement[1];
                    if (0 <= nr && nr < m && 0 <= nc && nc < n && grid[nr][nc] == 0 && !visited[nr][nc]) {
                        queue.add(new int[]{nr, nc});
                        visited[nr][nc] = true;
                    }
                }
            }
            ans++;
        }
        return -1;
    }
}