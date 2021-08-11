from typing import List
import math

class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        for i in reversed(range(1, int(math.sqrt(num + 3) + 1))):
            if (num + 1) % i == 0:
                return [i, (num + 1) // i]

            if (num + 2) % i == 0:
               return [i, (num + 2) // i]
        
a = Solution()
a.closestDivisors(8)