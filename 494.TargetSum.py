from collections import defaultdict

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = defaultdict(int)
        dp[0] = 1
        for n in nums:
            new = defaultdict(int)
            for key in dp:
                new[key + n] += dp[key]
                new[key - n] += dp[key]
            dp = new

        return dp[target]