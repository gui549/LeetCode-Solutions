class Solution:
    def reverse(self, x: int) -> int:
        s = str(x)
        ans = int(s[::-1]) if s[0] != '-' else int(s[0] + s[:0:-1])
        return ans if -(2 ** 31) <= ans <= 2 ** 31 - 1 else 0