from typing import List

class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        low_col, hi_col = 0, n - 1
        while low_col <= hi_col:
            mid_col = low_col + (hi_col - low_col) // 2
        
            max_row = 0
            for row in range(m):
                if mat[max_row][mid_col] < mat[row][mid_col]:
                    max_row = row

            bigger_than_left = (mid_col == 0) or (mat[max_row][mid_col] > mat[max_row][mid_col - 1])
            bigger_than_right = (mid_col == n - 1) or (mat[max_row][mid_col] > mat[max_row][mid_col + 1])

            if bigger_than_left and bigger_than_right:
                return [max_row, mid_col]
            elif bigger_than_left:
                low_col = mid_col + 1
            else:
                hi_col = mid_col - 1
            