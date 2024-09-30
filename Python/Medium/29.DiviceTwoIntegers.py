class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        ans = 0
        positive = (dividend > 0) is (divisor > 0)
        diff = len(bin(abs(dividend))) - len(bin(abs(divisor)))
        while abs(dividend) >= abs(divisor) and diff >= 0:
            if abs(dividend) >= abs(divisor) << diff:
                if positive:
                    dividend -= divisor << diff
                    ans += 1 << diff
                else:
                    dividend -= divisor << diff
                    ans += 1 << diff
            diff -= 1
   
        return min(ans, (1 << 31) - 1)