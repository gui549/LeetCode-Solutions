class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        ans = sum(n > 0 for row in grid for n in row)
                    
        for row in grid:
            ans += max(row)

        for col in zip(*grid):
            ans += max(col)

        return ans