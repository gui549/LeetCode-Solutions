from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dist = 0
        for i, num in enumerate(nums):
            if i > dist:
                return False
            dist = max(dist, i + num)
        
        return True

a = Solution()
a.canJump([3,2,1,0,4])