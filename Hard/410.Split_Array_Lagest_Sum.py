from typing import List

class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        lo, hi = 0, 10 ** 9
        while lo < hi:
            mid = lo + (hi - lo) // 2
            curr_sum, count = 0, 0
            for num in nums:
                if num > mid:
                    count = m + 1
                    break
                curr_sum += num
                if curr_sum > mid:
                    count += 1
                    curr_sum = num
            
            if count >= m:
                lo = mid + 1
            else:
                hi = mid
        
        return lo

