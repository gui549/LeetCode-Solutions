from functools import lru_cache
from typing import List


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs) // 2
        @lru_cache(None)
        def recursion(a, b):
            if a == n and b == n:
                return 0

            elif a == n:
                return recursion(a, b + 1) + costs[a + b][1]

            elif b == n:
                return recursion(a + 1, b) + costs[a + b][0]

            else:
                return min(recursion(a + 1, b) + costs[a + b][0], recursion(a, b + 1) + costs[a + b][1])

        return recursion(0, 0)
