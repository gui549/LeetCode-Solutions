from collections import Counter

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        counter, depth = Counter(), 0
        for c in s:
            if c == '(':
                depth += 1
            else:
                depth -= 1
                counter[depth] += counter[depth + 1] * 2 if counter[depth + 1] else 1
                del counter[depth + 1]

        return counter[0]

a = Solution()
a.scoreOfParentheses("(()(()))")