import re

# Refer to https://leetcode.com/problems/solve-the-equation/discuss/105362/Simple-2-liner-(and-more)
class Solution:
    def solveEquation(self, equation: str) -> str:
        side = 1
        a, b = 0, 0
        for eq, sign, c, x in re.findall('(=)|([-+]?)(\d*)(x?)', equation):
            if eq:
                side *= -1
            elif x:
                a += side * int(sign + '1') * int(c or 1)   
            elif c:
                b += side * int(sign + '1') * int(c)
            

        return f"x={-b // a}" if a else "No solution" if b else "Infinite solutions"
