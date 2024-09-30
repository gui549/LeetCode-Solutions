from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        needs = Counter(s1)
        l, r = 0, len(s1) - 1
        sub_elements = Counter(s2[l:r+1])
        while r < len(s2):
            
            if not needs - sub_elements:
                return True
            
            sub_elements[s2[r]] += 1
            sub_elements[s2[l]] -= 1

            l += 1
            r += 1

        return False

