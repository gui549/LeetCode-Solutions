class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        ans = 0
        for i in range(len(s)):
            for j in range(len(t)):
                if s[i] != t[j]:
                    l, r = 1, 1
                    while 0 <= i - l and 0 <= j - l and s[i - l] == t[j - l]:
                        l += 1
                    while i + r < len(s) and j + r < len(t) and s[i + r] == t[j + r]:
                        r += 1
                    ans += l * r
        return ans
                    