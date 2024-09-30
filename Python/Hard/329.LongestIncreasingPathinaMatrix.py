from typing import List

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        movement = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        answer = [[-1] * n for _ in range(m)]
        def bfs(x, y):
            if answer[x][y] != -1:
                return answer[x][y]

            for dx, dy in movement:
                if 0 <= x + dx < m and 0 <= y + dy < n and matrix[x][y] < matrix[x + dx][y + dy]:
                    answer[x][y] = max(answer[x][y], bfs(x + dx, y + dy) + 1)

            answer[x][y] = max(answer[x][y], 1)
            return answer[x][y]

        
        for x in range(m):
            for y in range(n):
                bfs(x, y)

        return max([max(row) for row in answer])

a = Solution()
print(a.longestIncreasingPath([[7,7,5],[2,4,6],[8,2,0]]))