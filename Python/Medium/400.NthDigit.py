class Solution:
    def findNthDigit(self, n: int) -> int:
        numDigit = 1
        count = 0
        while True:
            m = 9 * (10 ** (numDigit - 1)) * numDigit
            if n > m:
                n -= m
                numDigit += 1
            else:
                break
        
        subNth = (n - 1) // numDigit
        i = (n - 1) % numDigit 

        return str(10 ** (numDigit - 1) + subNth)[i] 


a = Solution()
print(a.findNthDigit(3))
