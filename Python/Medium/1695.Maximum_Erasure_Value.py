from typing import List

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        ans = curr_sum = 0
        subarr = set()
        l = r = 0
        for r in range(len(nums)):
            while nums[r] in subarr:
                subarr.remove(nums[l])
                curr_sum -= nums[l]
                l += 1

            curr_sum += nums[r]
            subarr.add(nums[r])

            ans = max(ans, curr_sum)
        
        return ans