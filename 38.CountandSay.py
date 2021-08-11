class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'

        ans = ''
        buffer, count = None, 0
        prevStr = self.countAndSay(n - 1)
        for c in prevStr:
            if c == buffer:
                count += 1
            else:
                if buffer: ans = ''.join([ans, str(count), buffer])
                buffer = c
                count = 1

        # print(ans, buffer, str(count))
        ans = ''.join([ans, str(count), buffer])
        print(ans)
        return ans

a = Solution()
a.countAndSay(10)