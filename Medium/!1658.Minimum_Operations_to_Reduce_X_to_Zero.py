from json import tool
from typing import List

class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        ans = 1e10
        total = sum(nums) - x
        if total < 0:
            return -1
        
        l, current_sum = 0, 0
        for r in range(len(nums)):
            current_sum += nums[r]
            while current_sum > total:
                current_sum -= nums[l]
                l += 1

            if current_sum == total:
                ans = min(ans, len(nums) - (r - l + 1))

        return ans if ans != 1e10 else -1