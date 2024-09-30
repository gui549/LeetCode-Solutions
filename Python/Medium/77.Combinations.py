from math import comb
from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if k == 0:
            return [[]]
        
        return [comb + [i] for i in range (k, n+1) for comb in self.combine(n - 1, k - 1)]