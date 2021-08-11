from typing import List
from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        pacific = [[False for j in range(n)] for i in range(m)]
        atlantic = [[False for j in range(n)] for i in range(m)]
        movement = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        def bfs(board, x, y):
            deq, visited = deque([(x, y)]), set()
            while deq:
                newX, newY = deq.popleft()
                if board[newX][newY] or (newX, newY) in visited:
                    continue
                
                board[newX][newY] = True
                visited.add((newX, newY))

                for dx, dy in movement:
                    if 0 <= newX + dx < m and 0 <= newY + dy < n and heights[newX][newY] <= heights[newX + dx][newY + dy]:
                        deq.append((newX + dx, newY + dy))

            return 

        # def bfs(board, visited, x, y):
        #     if board[x][y] or (x, y) in visited:
        #         return board[x][y]

        #     visited.add((x, y))

        #     for dx, dy in movement:
        #         if 0 <= x + dx < m and 0 <= y + dy < n and heights[x][y] >= heights[x + dx][y + dy]:
        #             board[x][y] = board[x][y] or bfs(board, visited, x + dx, y + dy)

        #     return board[x][y]
        
        for i in range(m):
            bfs(pacific, i, 0)
            bfs(atlantic, i, n - 1)

        for j in range(n):
            bfs(pacific, 0, j)
            bfs(atlantic, m - 1, j)

        ans = []
        for i in range(m):
            for j in range(n):
                if pacific[i][j] and atlantic[i][j]:
                    ans.append([i, j])

        return ans

a = Solution()
a.pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]])