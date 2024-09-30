from typing import List
from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ctr = Counter()
        for n in nums:
            ctr[n] += 1
            if len(ctr) == 2:
                ctr -= Counter(set(ctr))

        return list(ctr.keys())[0]