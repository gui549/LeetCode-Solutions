from typing import List
from itertools import accumulate

class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        ans = 0
        li = sorted(zip(difficulty, profit), key=lambda x: x[0])
        li = list(accumulate(li, lambda x, y: (y[0], max(x[1], y[1]))))
        for w in worker:
            if li[0][0] > w:
                continue
            lo, hi = 0, len(li) - 1
            while lo < hi:
                mid = lo + (hi - lo + 1) // 2
                if li[mid][0] <= w:
                    lo = mid
                else:
                    hi = mid - 1
  
            ans += li[lo][1]
            
        return ans

a = Solution()
print(a.maxProfitAssignment([2,4,6,8,10],[10,20,30,40,50],[4,5,6,7]))

