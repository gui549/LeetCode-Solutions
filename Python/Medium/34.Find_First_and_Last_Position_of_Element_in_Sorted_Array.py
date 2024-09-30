from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first = last = -1
        lo, hi = 0, len(nums) -1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] >= target:
                if nums[mid] == target:
                    first = mid
                hi = mid - 1
            else:
                lo = mid + 1
        lo, hi = 0, len(nums) -1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] <= target:
                if nums[mid] == target:
                    last = mid
                lo = mid + 1
            else:
                hi = mid - 1
        
        return [first, last]

""" 
NOTE
class Solution:
    def searchRange(self, nums, target):
        lo = bisect.bisect_left(nums, target)
        return [lo, bisect.bisect(nums, target)-1] if target in nums[lo:lo+1] else [-1, -1]
"""