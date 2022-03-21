from collections import Counter
from typing import List


class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.atMost(nums, k) - self.atMost(nums, k- 1)
    
    def atMost(self, nums, limit):
        ctr = Counter()
        res = l = 0
        for r in range(len(nums)):
            if ctr[nums[r]] == 0:
                limit -= 1

            ctr[nums[r]] += 1
            while limit > 0:
                ctr[nums[l]] -= 1
                if ctr[nums[l]] == 0:
                    limit += 1
                l += 1
            res += r - l + 1
        
        return res