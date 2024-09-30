### Shorter Coding ###

class Solution:
    def intToRoman(self, num: int) -> str:
        ans = ''
        characters = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        scope = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        for c, s in zip(characters, scope):
            if num // s:
                ans += c * (num // s)
                num = num % s
        
        return ans

a = Solution()
a.intToRoman(3)

### Hard coding ###

# class Solution:
#     def intToRoman(self, num: int) -> str:
#         ans = ''
#         while num > 0:
#             if num >= 1000:
#                 ans += 'M'
#                 num -= 1000
            
#             elif 1000 > num >= 900:
#                 ans += 'CM'
#                 num -= 900
            
#             elif 900 > num >= 500:
#                 ans += 'D'
#                 num -= 500

#             elif 500 > num >= 400:
#                 ans += 'CD'
#                 num -= 400

#             elif 400 > num >= 100:
#                 ans += 'C'
#                 num -= 100

#             elif 100 > num >= 90:
#                 ans += 'XC'
#                 num -= 90
            
#             elif 90 > num >= 50:
#                 ans += 'L'
#                 num -= 50

#             elif 50 > num >= 40:
#                 ans += 'XL'
#                 num -= 40
            
#             elif 40 > num >= 10:
#                 ans += 'X'
#                 num -= 10

#             elif num == 9:
#                 ans += 'IX'
#                 num -= 9
            
#             elif 9 > num >= 5:
#                 ans += 'V'
#                 num -= 5

#             elif num == 4:
#                 ans += 'IV'
#                 num -= 4
            
#             else:
#                 ans += 'I'
#                 num -= 1

#         return ans