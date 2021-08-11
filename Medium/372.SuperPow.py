from typing import List
from functools import reduce

class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        if a % 1337 == 0:
            return 0
        else:
            return pow(a, reduce(lambda x, y : (10 * x + y) % 1140, b), 1337)

a = Solution()
a.superPow(2, [3])