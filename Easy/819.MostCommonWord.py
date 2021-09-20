from typing import List
from re import sub
from collections import Counter 

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = sub("[!?,;.\"\']", " ", paragraph).lower().split()
        words = filter(lambda s: s not in banned, words)
        ctr = Counter(words)
        return ctr.most_common(1)[0][0]
        