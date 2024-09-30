from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]

        return [[nums[i]] + comb for i in range(len(nums)) for comb in self.permute(nums[:i] + nums[i + 1:])]