from typing import List

class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        ans = 0
        for i in points:
            dist_dict = dict()
            for point in points:
                dx = i[0] - point[0]
                dy = i[1] - point[1]
                dist_dict[dx ** 2 + dy ** 2] = 1 + dist_dict.get(dx ** 2 + dy ** 2, 0)
            for dist in dist_dict:
                ans += dist_dict[dist] * (dist_dict[dist] - 1)
                
        return ans

s = Solution()
s.numberOfBoomerangs([[1,8],[7,9],[2,0],[2,3],[7,5],[9,2],[2,8],[9,7],[3,6],[1,2]])
        