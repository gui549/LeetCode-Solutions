from typing import List

class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        current = sum(i * nums[i] for i in range(n))
        ans, total = current, sum(nums)
        for i in range(n):
            current = current + total - n * nums[~i] 
            ans = max(ans, current)

        return ans

s = Solution()
print(s.maxRotateFunction([4, 3, 2, 6]))


