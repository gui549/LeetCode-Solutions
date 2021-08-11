from typing import List
from collections import defaultdict

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1 # tail
        area = 0
        while l < r:
            area = max(area, (r - l) * min(height[r], height[l]))
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1

        return area

a = Solution()
print(a.maxArea([2,3,4,5,18,17,6]))