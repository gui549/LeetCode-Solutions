from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] == target:
                return True

            if (nums[lo] == nums[mid] and nums[hi] == nums[mid]): # ❗❗❗ : due to the exixstence of duplicates
                lo, hi = lo + 1, hi - 1
            
            elif nums[mid] >= nums[lo]:
                if nums[lo] <= target <= nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1

            else:
                if nums[mid] <= target <= nums[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1

        return False