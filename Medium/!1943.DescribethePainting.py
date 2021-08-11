from typing import List
from collections import defaultdict

class Solution:
    def splitPainting(self, segments: List[List[int]]) -> List[List[int]]:
        points = defaultdict(int)
        for s, e, c in segments:
            points[s] += c
            points[e] -= c

        ans, total = [], 0
        keys = sorted(points.keys())
        for i in range(len(keys) - 1):
            total += points[keys[i]]
            if total: ans.append([keys[i], keys[i + 1], total])

        return ans

a = Solution()
print(a.splitPainting([[1,7,9],[6,8,15],[8,10,7]]))
# print(a.splitPainting([[4,5,9],[8,12,5],[4,7,19],[14,15,1],[3,10,8],[17,20,18],[7,19,14],[8,16,6],[14,17,7],[11,13,3]]))

