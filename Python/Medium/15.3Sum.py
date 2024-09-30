from collections import Counter
from itertools import combinations_with_replacement
from typing import List


""" Original Solution
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        ctr = Counter(nums)
        for i, j in combinations_with_replacement(ctr, 2)
            ctr[i] -= 1
            ctr[j] -= 1
            if ctr[i] >= 0 and ctr[j] >= 0 and ctr[-(i + j)] >= 1:
                ans.add(tuple(sorted((i, j, -(i + j)))))
            ctr[i] += 1
            ctr[j] += 1

        return ans
"""

# Faster Solution
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        for i in range(len(nums)):
            if 0 < i and nums[i] == nums[i - 1]:
                continue

            target = -nums[i]
            l, r = i + 1, len(nums) - 1
            while l < r:
                if nums[l] + nums[r] == target:
                    ans.append((nums[i], nums[l], nums[r]))
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    
                elif nums[l] + nums[r] < target:
                    l += 1

                else:
                    r -= 1

        return ans