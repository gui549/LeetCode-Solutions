from typing import List
from collections import defaultdict

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        ans = 0
        substrings = defaultdict(list)
        
        for word in words:
            substrings[word[0]].append(word)
        
        for ch in s:
            target_substrings = substrings[ch]
            substrings[ch] = []
            for substring in target_substrings:
                if len(substring) == 1:
                    ans += 1
                else:
                    substrings[substring[1]].append(substring[1:])

        return ans