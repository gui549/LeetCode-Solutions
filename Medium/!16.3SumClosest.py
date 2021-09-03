from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = 9999
        for i in range(len(nums) - 2):
            j, k = i + 1, len(nums) - 1
            while j < k:
                current_sum = nums[i] + nums[j] + nums[k]
                if abs(target - ans) > abs(target - current_sum):
                    ans = current_sum

                if current_sum > target:
                    k -= 1
                elif current_sum < target:
                    j += 1
                else:
                    return ans

        return ans