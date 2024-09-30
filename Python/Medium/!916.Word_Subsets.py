from typing import List
from collections import Counter

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        ans = []
        words2_counter = Counter()
        
        for word2 in words2:
            words2_counter |= Counter(word2) # ❗❗❗
  
        min_length = sum(words2_counter.values())
        for word1 in words1:
            if len(word1) < min_length:
                continue

            if not words2_counter - Counter(word1): # ❗❗❗ Subtract is keeping only positive counts
                ans.append(word1)
    
        return ans

