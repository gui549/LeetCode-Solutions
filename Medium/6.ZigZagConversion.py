class Solution:
    def convert(self, s: str, numRows: int) -> str:
        ans = ''
        for r in range(numRows):
            i = r
            interval = max(2 * (numRows - 1), 1) 
            if r == 0 or r == numRows - 1:
                while i < len(s):
                    ans = ''.join([ans, s[i]])
                    i += interval
            else:
                first = True
                while i < len(s):
                    ans = ''.join([ans, s[i]])
                    i = i + interval - 2*r if first else i + 2*r
                    first = not first
    
        return ans

a = Solution()
a.convert('A', 1)