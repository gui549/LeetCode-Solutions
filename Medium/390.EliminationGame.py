class Solution:
    def lastRemaining(self, n: int) -> int:
        l2r = True
        fold = 0
        start = 1
        while n > 1:
            if l2r or n % 2 == 1:
                start = start + (2 ** fold)
            n = n // 2
            fold += 1
            l2r = not l2r

        return start

a = Solution()
print(a.lastRemaining(100))
