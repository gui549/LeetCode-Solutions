from typing import List

class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        ans = 1e9
        l, r, current_sum = 0, 0, 0
        dp = [1e9] * len(arr)

        for r in range(len(arr)):
            current_sum += arr[r]
            while current_sum > target:
                current_sum -= arr[l]
                l += 1
            
            if current_sum == target:
                ans = min(ans, dp[l - 1] + r - l + 1)
                dp[r] = min(dp[r - 1], r - l + 1)
            else:
                dp[r] = dp[r - 1]

        return ans if ans != 1e9 else -1