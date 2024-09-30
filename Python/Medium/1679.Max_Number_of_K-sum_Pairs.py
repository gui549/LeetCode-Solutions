from collections import Counter
from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        ans = 0
        ctr = Counter(nums)
        for key in ctr:
            ans += min(ctr[key], ctr[k - key])

        return ans // 2