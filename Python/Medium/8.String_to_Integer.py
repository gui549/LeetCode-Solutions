class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0
        
        sign, chars = "", []
        if s[0] == '+' or s[0] == '-':
            sign = s[0]
            s = s[1:]
        
        for i in range(len(s)):
            if not ('0' <= s[i] <= '9'):
                break
            chars.append(s[i])

        if not chars:
            return 0

        ans = int(sign + "".join(chars))
        if ans < -(2  ** 31):
            ans = -(2 ** 31)
        elif ans > 2 ** 31 - 1:
            ans = 2 ** 31 - 1
        return ans 