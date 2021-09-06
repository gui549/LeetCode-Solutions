from typing import List

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        for i, c in enumerate(costs):
            if coins >= c:
                coins -= c
            else:
                return i