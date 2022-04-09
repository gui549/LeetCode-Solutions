from audioop import reverse
from typing import List

# Better Solution
class Solution:
    def trap(self, height: List[int]) -> int:
        water_level = []
        left = 0
        for h in height:
            left = max(left, h)
            water_level.append(left)
        right = 0
        for i, h in reversed(list(enumerate(height))):
            right = max(right, h)
            water_level[i] = min(water_level[i], right) - h
        return sum(water_level)


""" First Solution 
class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        left_height = [0] * len(height)
        right_height = [0] * len(height)
        left_height[0], right_height[-1] = height[0], height[-1]
        for i in range(1, len(height)):
            left_height[i] = max(left_height[i - 1], height[i])

        for i in range(len(height) - 2, -1, -1):
            right_height[i] = max(right_height[i + 1], height[i])

        for i in range(len(height)):
            ans += max(min(left_height[i], right_height[i]) - height[i], 0)

        return ans
"""