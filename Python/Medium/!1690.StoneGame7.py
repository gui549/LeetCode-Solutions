from typing import List
from itertools import accumulate

class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        prefix_sum = [0] + list(accumulate(stones))
        n = len(stones)
        dp = [[0] * n for _ in range(n)]
        def recursion(i, j):
            if i >= j:
                return 0
            
            if dp[i][j]:
                return dp[i][j]
            
            current = prefix_sum[j + 1] - prefix_sum[i] 
            score = max(current - stones[i] - recursion(i + 1, j), current - stones[j] - recursion(i, j - 1))

            dp[i][j] = score
            return dp[i][j]

        return recursion(0, n - 1)