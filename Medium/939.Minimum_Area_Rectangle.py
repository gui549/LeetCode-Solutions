from collections import Counter
from typing import List

class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        ans = 1e10
        seen = set()

        for x1, y1 in points:
            for x2, y2 in seen:
                area = abs(x1 - x2) * abs(y1 - y2)
                if area:
                    ans = min(ans, area)

        return ans if ans != 1e10 else 0