import math
from typing import List
from collections import Counter

class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        ans = 0
        counter = Counter()
        for w, h in rectangles:
            counter[w / h] += 1
        
        for freq in counter.values():
            ans += freq * (freq - 1) // 2

        return ans