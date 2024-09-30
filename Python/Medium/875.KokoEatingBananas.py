from typing import List
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        while l < r:
            speed = l + (r - l) // 2
            take = sum([math.ceil(p / speed) for p in piles])
            if take > h:
                l = speed + 1
            else:
                r = speed
        
        return l

a = Solution()
a.minEatingSpeed([3,6,7,11],8)
a.minEatingSpeed([30,11,23,4,20]
,5)
a.minEatingSpeed([30,11,23,4,20]
,6)

