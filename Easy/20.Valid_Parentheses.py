class Solution:
    def isValid(self, s: str) -> bool:
        d = {')' : '(', '}': '{', ']': '['}
        stack = []
        for ch in s:
            if ch == '(' or ch == '{' or ch =='[':
                stack.append(ch)
            else:
                if not stack or stack[-1] != d[ch]:
                    return False
                else:
                    stack.pop()
        return not stack