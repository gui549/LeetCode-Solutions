from typing import List
from collections import defaultdict

class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        cache = defaultdict(lambda: -1)
        total = sum(nums)
        def recursion(nums):
            if len(nums) == 1:
                return nums[0]

            elif len(nums) == 2:
                return max(nums)

            key = tuple(nums)
            if cache[key] != -1:
                return cache[key]
                
            cache[key] = max(nums[0] + min(recursion(nums[1:-1]), recursion(nums[2:])),
            nums[-1] + min(recursion(nums[1:-1]), recursion(nums[:-2])))

            return cache[key]

        return total <= recursion(nums) * 2

a = Solution()
a.PredictTheWinner([0])