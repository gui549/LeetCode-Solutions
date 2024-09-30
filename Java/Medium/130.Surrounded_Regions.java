package Medium;

class Solution {
    
    int[][] movements = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
    
    public void solve(char[][] board) {
        int m = board.length, n = board[0].length;
        for (int i = 0; i < m; i++) {
            if (board[i][0] == 'O') dfs(board, i, 0);
            if (board[i][n - 1] == 'O') dfs(board, i, n - 1);
        }

        for (int j = 1; j < n - 1; j++) {
            if (board[0][j] == 'O') dfs(board, 0, j);
            if (board[m - 1][j] == 'O') dfs(board, m - 1, j);
        }

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (board[i][j] == 'O') board[i][j] = 'X';
                else if (board[i][j] == 'N') board[i][j] = 'O'; 
            }
        }
    }

    public void dfs(char[][] board, int r, int c) {
        int m = board.length, n = board[0].length;
        board[r][c] = 'N';
        for (int[] movement : movements) {
            int nr = r + movement[0];
            int nc = c + movement[1];
            if (0 <= nr && nr < m && 0 <= nc && nc < n && board[nr][nc] == 'O') {
                dfs(board, nr, nc);
            }
        }
    }
}