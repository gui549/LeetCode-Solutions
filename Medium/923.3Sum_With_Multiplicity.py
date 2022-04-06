from collections import Counter
from itertools import combinations_with_replacement
from typing import List

class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        ans, mod = 0, 1000000007
        ctr = Counter(arr)
        for i, j in combinations_with_replacement(ctr, 2):
            k = target - i - j
            if i == j == k:
                ans += ctr[i] * (ctr[i] - 1) * (ctr[i] - 2) // 6
            elif i == j != k:
                ans += ctr[i] * (ctr[i] - 1) * ctr[k] // 2
            elif k > i and k > j:
                ans += ctr[i] * ctr[j] * ctr[k]
        return ans % mod


""" First Soultion
class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        mod = 1000000007
        ans = 0
        ctr = Counter(arr)
        sorted_key = sorted(ctr)
        for i in range(len(sorted_key)):
            if sorted_key[i] > target:
                break

            for j in range(i + 1):
                if sorted_key[i] + sorted_key[j] > target:
                    break

                for k in range(j + 1):
                    if sorted_key[i] + sorted_key[j] + sorted_key[k] > target:
                        break
                    
                    elif sorted_key[i] + sorted_key[j] + sorted_key[k] == target:
                        num1, num2, num3 = sorted_key[i], sorted_key[j], sorted_key[k]
                        if num1 == num2 == num3 and ctr[num1] >= 3:
                            ans += ctr[num1] * (ctr[num1] - 1) * (ctr[num1] - 2) // 6 % mod
                        
                        elif num1 == num2 != num3 and ctr[num1] >= 2:
                            ans += (ctr[num1] * (ctr[num1] - 1) // 2) * ctr[num3] % mod

                        elif num1 != num2 == num3 and ctr[num2] >= 2:
                            ans += (ctr[num2] * (ctr[num2] - 1) // 2) * ctr[num1] % mod

                        elif num1 != num2 != num3:
                            ans += ctr[num1] * ctr[num2] * ctr[num3] % mod

        return ans
"""