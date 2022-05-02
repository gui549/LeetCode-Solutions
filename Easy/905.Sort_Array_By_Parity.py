from typing import List

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        last_even = 0;
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                nums[i], nums[last_even] = nums[last_even], nums[i]
                last_even += 1
        return nums 