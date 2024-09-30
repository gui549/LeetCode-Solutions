from typing import List

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def trans(str):
            h, m = str.split(':')
            return int(h) * 60 + int(m)

        li = sorted([trans(time) for time in timePoints])
        ans = 1440
        for i in range(len(li)):
            if i == len(li):
                ans = min(ans, 1440 + li[0] - li[i])
            else:
                ans = min(ans, li[i + 1] - li[i])
            
        return ans

a = Solution()
print(a.findMinDifference(["12:12","00:13"]))