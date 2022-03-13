from typing import List
from collections import Counter, deque

class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        ctr = Counter(nums)

        for key in sorted(ctr):
            count = ctr[key]
            if count > 0: # if this condition doesn't exist, TLE occured.
                for i in range(k):
                    if ctr[key + i] >= count:
                        ctr[key + i] -= count
                    else:
                        return False
        
        return True