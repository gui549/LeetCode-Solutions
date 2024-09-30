from typing import List
from math import gcd

class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        while len(nums) > 1:
            r = gcd(nums.pop(), nums.pop())
            if r == 1:
                return True
            nums.append(r)
        return nums[0] == 1

a = Solution()
a.isGoodArray([1,5,8,2])