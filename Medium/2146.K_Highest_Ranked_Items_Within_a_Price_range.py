from collections import deque
import heapq
from typing import List

class Solution:
    def highestRankedKItems(self, grid: List[List[int]], pricing: List[int], start: List[int], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        movements = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        que = deque([[0, start]])
        ans, visited = [], set()

        while que:
            dist, (x, y) = que.popleft()

            if (x, y) in visited:
                continue

            visited.add((x, y))

            if pricing[0] <= grid[x][y] <= pricing[1]:
                heapq.heappush(ans, (dist, grid[x][y], (x, y)))


            for dx, dy in movements:
                if 0 <= x + dx < m and 0 <= y + dy < n and grid[x + dx][y + dy]:
                    que.append([dist + 1, (x + dx, y + dy)])

        return [heapq.heappop(ans)[2] for _ in range(min(k, len(ans)))]