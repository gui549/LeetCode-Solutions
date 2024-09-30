from typing import List
import math

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        ans = 0 
        h, t = 1, position[-1] - position[0]
        while h <= t:
            distance = int((h + t) / 2) # 1, 100 => 50
            temp, count = 0, 1
            for i in range(len(position)):
                if position[i] - position[temp] >= distance:
                    temp = i
                    count += 1
            if count >= m:
                ans = max(ans, distance)
                h = distance + 1
            elif count < m:
                t = distance - 1

        return ans


a = Solution()

# print(a.maxDistance([1,2,3,4,7], 3))
# print(a.maxDistance([1,2,3,4,5, 100], 2))
# print(a.maxDistance([1,2,3,4,5,6,7,8,9,10], 4))