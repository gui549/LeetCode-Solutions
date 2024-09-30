from typing import List

class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        ans = 0
        exist = set()     
        for startWord in startWords:
            bitmask = 0
            for ch in startWord:
                bitmask ^= 1 << ord(ch) - ord('a')
            exist.add(bitmask)

        
        for targetWord in targetWords:
            bitmask = 0
            for ch in targetWord:
                bitmask ^= 1 << ord(ch) - ord('a')
            for ch in targetWord:
                if bitmask ^ (1 << ord(ch) - ord('a')) in exist:
                    ans += 1
                    break
        
        return ans