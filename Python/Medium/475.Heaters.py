class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses = sorted(houses)
        heaters = sorted(heaters)
        ans = 0
        l, r = 0, 0
        while l < len(houses):
            subAns = abs(houses[l] - heaters[r])
            while r < len(heaters) - 1:
                if subAns < abs(houses[l] - heaters[r + 1]):
                    break
                
                subAns = abs(houses[l] - heaters[r + 1])
                r += 1

          
            ans = max(ans, subAns)
            l += 1

        return ans