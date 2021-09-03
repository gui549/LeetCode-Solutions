from typing import List

# Refer to https://leetcode.com/problems/self-crossing/discuss/79141/Another-python...
class Solution:
    def isSelfCrossing(self, distance: List[int]) -> bool:
        b = c = d = e = f = 0
        for a in distance:
            if d >= b > 0 and (a >= c or a >= c - e >= 0 and f >= d - b):
                print(a, b, c, d, e, f)
                return True
            b, c, d, e, f = a, b, c, d, e

        return False

a = Solution()
print(a.isSelfCrossing([1,2,3,4]))
# print(a.isSelfCrossing([1,1,2,2,5,2,2,1,1]))