from collections import Counter
from typing import List

class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        ctr = Counter()
        for num in arr:
            ctr[num] = ctr[num - difference] + 1
            
        return ctr.most_common()[0][1]

s = Solution()
s.longestSubsequence([-11,8,8,-13,-4,6,7,-3,8,4,-9,-7,13,-15,9], 9)