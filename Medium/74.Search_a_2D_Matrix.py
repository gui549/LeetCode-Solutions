from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lo, hi = 0, len(matrix) * len(matrix[0]) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            mid_row, mid_col = mid // len(matrix), mid % len(matrix)
            if matrix[mid_row][mid_col] == target:
                return True
            elif matrix[mid_row][mid_col] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return False        
