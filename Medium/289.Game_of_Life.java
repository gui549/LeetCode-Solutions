package Medium;

class Solution {
    public void gameOfLife(int[][] board) {
        int m = board.length, n = board[0].length;
        int[][] movements = { {0, 1}, {0, -1}, {1, 0}, {-1, 0}, 
                              {1, 1}, {1, -1}, {-1, 1}, {-1, -1} };
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                int count = 0;
                for (int[] movement : movements) {
                    int x = i + movement[0], y = j + movement[1];
                    if (0 <= x && x < m && 0 <= y && y < n) {
                        if (board[x][y] == 1 || board[x][y] == -1) count++;
                    }
                }
                if (count < 2) {
                    if (board[i][j] == 1) board[i][j] = -1;
                } else if (count == 3) {
                    if (board[i][j] == 0) board[i][j] = -2;
                } else if (4 <= count) {
                    if (board[i][j] == 1) board[i][j] = -1;
                }
            }
        }

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (board[i][j] == -1) board[i][j] = 0;
                else if (board[i][j] == -2) board[i][j] = 1;
            }
        }
    }
}