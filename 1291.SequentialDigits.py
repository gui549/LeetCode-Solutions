from typing import List

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        ans, head, digits, temp = [], 0, 1, low
        while temp // 10:
            digits += 1
            temp = temp // 10
        head = temp
        while True:
            current = 0
            if head + digits > 10:
                head = 1
                digits += 1

            for i in range(0, digits):
                current += (head + i) * (10 ** (digits - i - 1))
            
            if current > high:
                break
            
            elif current < low:
                head += 1
                
            else:
                ans.append(current)
                head += 1

        return ans


a = Solution()
print(a.sequentialDigits(58, 155))

# class Solution:
#     def sequentialDigits(self, low: int, high: int) -> List[int]:
#         allNums = [12,23,34,45,56,67,78,89,
#                 123,234,345,456,567,678,789,
#                 1234,2345,3456,4567,5678,6789,
#                 12345,23456,34567,45678,56789,
#                 123456,234567,345678,456789,
#                 1234567,2345678,3456789,
#                 12345678,23456789,
#                 123456789]

#         ans = []
#         for num in allNums:
#             if low < num < high:
#                 ans.append(num)
#             elif num > high:
#                 break

#         return ans