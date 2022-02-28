from typing import List
from collections import Counter

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        ans = 0
        counter = Counter(nums)
        for key in sorted(counter):
            if k == 0:
                if counter[key] > 1:
                    ans += 1

            else: 
                if counter[key + k] > 0:
                    ans += 1

        return ans
