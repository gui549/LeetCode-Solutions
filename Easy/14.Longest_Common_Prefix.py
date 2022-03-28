from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s1 = max(strs) # ❗
        s2 = min(strs) # ❗

        for i, ch in enumerate(s2):
            if ch != s1[i]:
                return s2[:i]

        return s2
            