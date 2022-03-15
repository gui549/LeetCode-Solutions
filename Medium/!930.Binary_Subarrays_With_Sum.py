from typing import List

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def at_most(value):
            if value == 0:
                return 0

            res, l = 0, 0
            for r in range(len(nums)):
                value -= nums[r]
                while value < 0:
                    value += nums[l]
                    l += 1
                res = r - l + 1
            return res
        return at_most(goal) - at_most(goal - 1)
            
