from typing import List
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def BFS(grid, point, visited):
            m, n = len(grid), len(grid[0])
            deq = deque()
            deq.append(point)
            movement = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            while len(deq) > 0:
                x, y = deq.popleft()
                if (x, y) in visited:
                    continue
                visited.add((x, y))
                [deq.append((x + dx, y + dy)) for dx, dy in movement if m > (x + dx) >= 0 and n > (y + dy) >= 0 and grid[x + dx][y + dy] == "1"]
        
        visited = set()
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1" and (i, j) not in visited:
                    BFS(grid, (i, j), visited)
                    count += 1
                else:
                    continue
        
        return count

a = Solution()
a.numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]])
        