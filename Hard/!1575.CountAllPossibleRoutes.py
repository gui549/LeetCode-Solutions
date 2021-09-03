from functools import lru_cache
from typing import List

class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        @lru_cache(None)
        def recursion(currentCity, fuel):
            if fuel < 0:
                return 0

            ans = 1 if currentCity == finish else 0
            for city in range(len(locations)):
                if currentCity != city:
                    ans += recursion(city, fuel - abs(locations[currentCity] - locations[city]))
            
            return ans

        return recursion(start, fuel) % 1000000007

a = Solution()
a.countRoutes([2,3,6,8,4],1,3,5)