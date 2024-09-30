from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ans = "@" + s
        need, current_window = Counter(t), Counter()
        l, r = 0, 0
        while r < len(s):
            current_window[s[r]] += 1
            while not (need - current_window) and l <= r:
                if r + 1 - l < len(ans):  
                    ans = s[l:r + 1]
                current_window[s[l]] -= 1
                l += 1

            r += 1

        return ans if ans != "@" + s else "" 

