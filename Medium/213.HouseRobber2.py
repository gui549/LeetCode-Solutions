from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return max(nums)

        dp1 = [0] * n # use nums[0]
        dp2 = [0] * n # not use nums[0]
        dp1[0] = nums[0]
        for i in range(1, n - 1):
            dp1[i] = max(dp1[i - 1], dp1[i - 2] + nums[i])
            dp2[i] = max(dp2[i - 1], dp2[i - 2] + nums[i])

        dp2[n - 1] = max(dp2[n - 2], dp2[n - 3] + nums[n - 1])

        return max(dp1[-2], dp2[-1])

a = Solution()
a.rob([2,2,4,3,2,5])