from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for str in strs:
            groups[tuple(sorted(str))].append(str)

        return list(groups.values())
            