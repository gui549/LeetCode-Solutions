class Solution:
    def minSwaps(self, s: str) -> int:
        stack = []
        for c in s:
            if c == '[':
                stack.append('[')
            else:
                if stack and stack[-1] == '[':
                    stack.pop()
                else:
                    stack.append(']')
        l = len(stack) // 2
        return l // 2 + l % 2