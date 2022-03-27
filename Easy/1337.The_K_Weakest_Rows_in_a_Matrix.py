import heapq
from typing import List

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        li = [(sum(row), idx) for idx, row in enumerate(mat)]
        return [x[1] for x in heapq.nsmallest(k, li)]
