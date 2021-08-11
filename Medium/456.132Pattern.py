from typing import List
from itertools import accumulate

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        minValue = list(accumulate(nums, min))
        stack = []

        for i in range(len(nums) - 1, -1, -1):
            while stack and stack[-1] <= minValue[i]:
                stack.pop()
            if stack and stack[-1] < nums[i]:
                return True
            stack.append(nums[i])

        return False

a = Solution()
print(a.find132pattern([3,1,2]))