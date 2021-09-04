from typing import List

class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        current, ans = 0, 0
        for rung in rungs:
            ans += (rung - current - 1) // dist
            current = rung
        
        return ans