from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def recursion(left, stack):
            if not left:
                return [")" * stack]

            ans = []
            for s in recursion(left - 1, stack + 1):
                ans.append("(" + s)
            
            if stack:
                for s in recursion(left, stack - 1):
                    ans.append(")" + s)

            return ans
        return recursion(n, 0)