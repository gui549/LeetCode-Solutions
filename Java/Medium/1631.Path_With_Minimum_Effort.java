package Medium;

import java.util.Arrays;
import java.util.Comparator;
import java.util.PriorityQueue;

// better solution
class Solution {
    public int minimumEffortPath(int[][] heights) {
        int m = heights.length, n = heights[0].length;
        int[][] movements = { {0, 1}, {0, -1}, {1, 0}, {-1, 0} };
        int[][] dist = new int[m][n];
        for (int i = 0; i < m; i++) Arrays.fill(dist[i], Integer.MAX_VALUE);

        PriorityQueue<int[]> minHeap = new PriorityQueue<>(Comparator.comparingInt(a -> a[0]));
        minHeap.offer(new int[]{0, 0, 0});
        while (!minHeap.isEmpty()) {
            int[] top = minHeap.poll();
            int d = top[0], r = top[1], c = top[2];
            if (d > dist[r][c]) continue;
            if (r == m - 1 && c == n - 1) return d;
            for (int[] movement : movements) {
                int newR = r + movement[0], newC = c + movement[1];
                if (0 <= newR && newR < m && 0 <= newC && newC < n) {
                    int newDist = Math.max(d, Math.abs(heights[newR][newC] - heights[r][c]));
                    if (dist[newR][newC] > newDist) {
                        dist[newR][newC] = newDist;
                        minHeap.offer(new int[]{dist[newR][newC], newR, newC});
                    }
                }
            }
        }
        return 0;
    }
}

// first solution
// class Solution {
//     public int minimumEffortPath(int[][] heights) {
//         int ans = 0;
//         int m = heights.length, n = heights[0].length;
//         int[][] movements = { {0, 1}, {0, -1}, {1, 0}, {-1, 0} };
//         boolean[][] visited = new boolean[m][n];

//         PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(i -> i[2]));
//         pq.add(new int[]{0, 0, 0});
//         while(!pq.isEmpty()) {
//             int[] currentCell = pq.poll();
//             ans = Math.max(ans, currentCell[2]);
//             if (currentCell[0] == m - 1 && currentCell[1] == n - 1) return ans;
//             if (visited[currentCell[0]][currentCell[1]]) continue;
//             else visited[currentCell[0]][currentCell[1]] = true;

//             for (int[] movement : movements) {
//                 int nextX = currentCell[0] + movement[0];
//                 int nextY = currentCell[1] + movement[1];
//                 if (0 <= nextX && nextX < m && 0 <= nextY && nextY < n && !visited[nextX][nextY]) {
//                     int diff = Math.abs(heights[nextX][nextY] - heights[currentCell[0]][currentCell[1]]);
//                     pq.add(new int[]{ nextX, nextY, diff });
//                 }
//             }
//         }
//         return ans;
//     }
// }