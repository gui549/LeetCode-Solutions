from typing import List
from collections import Counter

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        ans = 0
        counter, same_letters = Counter(), 0
        for word in words:
            if word[0] == word[1]:
                if counter[word]:
                    counter[word] -= 1
                    same_letters -= 1
                    ans += 4
                else:
                    counter[word] += 1
                    same_letters += 1

            else:
                if counter[word[::-1]]:
                    counter[word[::-1]] -= 1
                    ans += 4
                else:
                    counter[word] += 1

        ans += 2 * (same_letters > 0)
        return ans