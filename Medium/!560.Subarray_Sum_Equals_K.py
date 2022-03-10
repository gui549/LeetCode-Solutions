from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        prefix_sum, freq = [0], {0: 1}
        
        for i in range(len(nums)):
            n = prefix_sum[-1] + nums[i]
            prefix_sum.append(n)
            ans += freq.get(n - k, 0)
            freq[n] = freq.get(n, 0) + 1

        return ans