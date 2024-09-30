class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        if len(num) < 3:
            return False

        def recursion(l, m, r):
            s1, s2, s3 = num[l:m], num[m:r], num[r:]
            s4 = str(int(s1) + int(s2)) 
            if s1 != str(int(s1)) or s2 != str(int(s2)):
                return False
            
            if len(s3) >= len(s4):
                if s3.find(s4) == 0:
                    if r + len(s4) == len(num):
                        return True
                    else:
                        return recursion(m, r, r + len(s4))
            
            return False

        l, m, r = 0, 1, 2
        while m < len(num):
            if recursion(l, m, r):
                return True
            
            if r == len(num) + 1:
                m += 1
                r = m
            
            r += 1
        
        return False

# Refer to https://leetcode.com/problems/additive-number/discuss/75578/Python-solution
from itertools import combinations

# class Solution:
#     def isAdditiveNumber(self, num: str) -> bool:
#         if len(num) < 3:
#             return False

#         for l, r in combinations(range(1, len(num)), 2):
#             s1, s2 = num[:l], num[l:r]
#             if s1 != str(int(s1)) or s2 != str(int(s2)):
#                 continue
            
#             while r < len(num):
#                 s3 = str(int(s1) + int(s2)) 
#                 if not num.startswith(s3, r):
#                     break
#                 r += len(s3)
#                 if r == len(num):
#                     return True
#                 s1, s2 = s2, s3
            
#         return False

a = Solution()
print(a.isAdditiveNumber("199111992"))