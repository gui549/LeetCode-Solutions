from collections import deque

class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        ans = 0
        while target > startValue:
            ans += 1 + target % 2
            target = (target + 1) // 2

        return ans + startValue - target