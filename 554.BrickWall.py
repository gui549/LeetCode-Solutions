from typing import List
from collections import defaultdict

class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        n, m = len(wall), sum(wall[0])
        col = defaultdict(int)
        for row in wall:
            start = 0
            for i in range(len(row) - 1):
                start += row[i]
                col[start] += 1

        if col.values():     
            return n - max(col.values())

        return n

a = Solution()
a.leastBricks([[1,1],[2],[1,1]])