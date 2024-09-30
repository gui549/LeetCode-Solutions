from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [987654321] * len(nums)
        dp[0] = 0
        for i in range(len(dp)):
            for j in range(i, min(i + nums[i] + 1, len(nums))):
                dp[j] = min(dp[i] + 1, dp[j])

        return dp[-1]