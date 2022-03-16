from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        ctr1, ctr2 = Counter(word1), Counter(word2) 

        return set(word1) == set(word2) and Counter(ctr1.values()) == Counter(ctr2.values())
