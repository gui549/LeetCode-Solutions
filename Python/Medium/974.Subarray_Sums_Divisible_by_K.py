from typing import List
from collections import Counter

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        ans = current_sum = 0
        prefix = Counter()
        for num in nums:
            current_sum += num
            ans += prefix[k - (current_sum % k)]
            prefix[current_sum % k] += 1

        return ans