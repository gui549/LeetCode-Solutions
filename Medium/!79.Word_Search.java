package Medium;

class Solution {
    int[][] movements = { {0, 1}, {0, -1}, {1, 0}, {-1, 0} };

    public boolean exist(char[][] board, String word) {
        for (int i = 0; i <= board.length; i++) {
            for (int j = 0; j <= board[0].length; j++) {
                if (dfs(board, i, j, word, 0)) return true;
            }
        }
        return false;
    }

    private boolean dfs(char[][] board, int x, int y, String word, int len) {
        if (len == word.length()) return true;
        if (!(0 <= x && x < board.length && 0 <= y && y < board[0].length 
            && board[x][y] == word.charAt(len))) return false;
        board[x][y] = '*';
        boolean res = false;
        for (int[] movement : movements) {
            res |= dfs(board, x + movement[0], y + movement[1], word, len + 1);
        }
        board[x][y] = word.charAt(len);
        return res;
    }
}