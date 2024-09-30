from typing import List
from collections import Counter

class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        delta = Counter()
        for i in range(len(nums) // 2):
            a, b = nums[i], nums[~i]
            delta[2] += 2
            delta[min(a, b) + 1] -= 1
            delta[a + b] -= 1
            delta[a + b + 1] += 1
            delta[max(a, b) + limit + 1] += 1

        ans, moves = 1234567890, 0
        for target_sum in range(2, limit * 2 + 1):
            moves += delta[target_sum]
            ans = min(ans, moves)

        return ans