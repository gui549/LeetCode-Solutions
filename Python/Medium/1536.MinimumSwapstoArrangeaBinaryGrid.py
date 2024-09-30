from typing import List

class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        def countZero(list):
            count = 0
            for i in list[::-1]:
                if i == 1: break
                count += 1
            return count
    
        zeroCount = [countZero(g) for g in grid]
        
        n, answer = len(grid), 0
        for i in range(n):
            found = False
            for j in range(len(zeroCount)):
                if n - 1 - i <= zeroCount[j]:
                    answer += j
                    zeroCount.pop(j)
                    found= True
                    break
            if not found:
                return -1
                
        return answer