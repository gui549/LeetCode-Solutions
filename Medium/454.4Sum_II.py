from typing import List
from collections import Counter

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        ans = 0
        counter = Counter()
        for n in nums1:
            for m in nums2:
                counter[n + m] += 1

        for n in nums3:
            for m in nums4:
                ans += counter[0 - (n + m)]

        return ans