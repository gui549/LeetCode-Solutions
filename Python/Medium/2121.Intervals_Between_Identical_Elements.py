from collections import defaultdict
from typing import List


class Solution:
    def getDistances(self, arr: List[int]) -> List[int]:
        ans = [0] * len(arr)
        indices = defaultdict(list)
        for i, num in enumerate(arr):
            indices[num].append(i)

        for value in indices:
            total = sum(indices[value])
            after = 0
            for i, idx in enumerate(indices[value]):
                ans[idx] = total - idx * (len(indices[value]) - 2 * i) - 2 * after
                after += idx

        return ans