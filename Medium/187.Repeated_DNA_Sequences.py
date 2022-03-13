from typing import List
from collections import Counter

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        ctr = Counter()
        for i in range(len(s) - 9):
            ctr[s[i:i+10]] += 1

        ans = []
        for key in ctr:
            if ctr[key] > 1:
                ans.append(key)

        return ans