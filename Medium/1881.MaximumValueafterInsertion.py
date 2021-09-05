class Solution:
    def maxValue(self, n: str, x: int) -> str:
        if n[0] == '-':
            for i in range(1, len(n)):
                if n[i] < str(x):
                    return n[:i] + str(x) + n[i:]
        else:
            for i in range(len(n)):
                if n[i] < str(x):
                    return n[:i] + str(x) + n[i:]