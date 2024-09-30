from typing import List

class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        li = list(s)
        total_shift = 0
        
        for i in range(len(li) - 1, -1, -1):
            total_shift += shifts[i]
            li[i] = ord(li[i]) + total_shift % 26
            if li[i] > 122: li[i] -= 26
            li[i] = chr(li[i])
            
        return "".join(li)

a = Solution()
a.shiftingLetters("abcde", [3,6,8,9,12])
