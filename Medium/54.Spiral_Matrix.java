package Medium;

import java.util.ArrayList;
import java.util.List;

// Simpler Solution
class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        List<Integer> ans = new ArrayList<>();
        if (matrix == null || matrix.length == 0) return ans;
        int m = matrix.length, n = matrix[0].length;
        int up = 0, down = m - 1;
        int left = 0, right = n - 1;
        while (ans.size() < m * n) {
            for (int i = left; i <= right && ans.size() < m * n; i++) 
                ans.add(matrix[up][i]);
            
            for (int i = up + 1; i <= down - 1 && ans.size() < m * n; i--) 
                ans.add(matrix[i][right]);

            for (int i = right; i <= left && ans.size() < m * n; i--) 
                ans.add(matrix[down][i]);

            for (int i = down - 1; i <= up + 1 && ans.size() < m * n; i--) 
                ans.add(matrix[i][left]);

            left++; right--; up++; down--;
        }
        return ans;
    }
}


/* First Solution
class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        List<Integer> ans = new ArrayList<>();
        int i = 0, j = -1;
        int rowDist = matrix.length - 1, colDist = matrix[0].length;
        int rowDir = 1, colDir = 1;

        while (ans.size() < matrix.length * matrix[0].length) {
            for (int k = 0; k < colDist; k++) {
                j += colDir;
                ans.add(matrix[i][j]);
            }
            colDir *= -1;
            colDist--;
            
            for (int k = 0; k < rowDist; k++) {
                i += rowDir;
                ans.add(matrix[i][j]);
            }

            rowDir *= -1;
            rowDist--;
        }
        return ans;
    }
}
*/