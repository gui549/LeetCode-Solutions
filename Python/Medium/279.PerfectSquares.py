from math import sqrt

class Solution:
    def numSquares(self, n: int) -> int:
        squares = [i * i for i in range(1, int(sqrt(n)) + 1)]
        dp = [0] * (n + 1)
        for i in range(1, len(dp)):
            dp[i] = min([dp[i - s] + 1 for s in squares if s <= i])

        return dp[n]

a = Solution()
a.numSquares(13)