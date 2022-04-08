from itertools import permutations
from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def recursion(curr, candidates):
            if not candidates:
                ans.append(curr)
            
            for i in range(len(candidates)):
                recursion(curr + [candidates[i]], candidates[:i] + candidates[i+1:])

        recursion([], nums)
        return ans