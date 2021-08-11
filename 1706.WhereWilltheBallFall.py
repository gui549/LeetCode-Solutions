from typing import List

class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        def calc(list):
            res = [None] * len(list) 
            for i in range(len(list)):
                if res[i] == 0: 
                    continue
                if i == 0 and list[i] == -1:
                    res[i] = 0
                    continue
                if i == len(list) - 1 and list[i] == 1:
                    res[i] = 0
                    continue
                if list[i] == 1 and list[i + 1] == -1:
                    res[i] = 0
                    res[i + 1] = 0
                if res[i] != 0:
                    res[i] = list[i]
            
            return res
        
        m, n = len(grid), len(grid[0])
        movement = [calc(g) for g in grid]
        print(movement)
        balls = [[0, i] for i in range(n)]
        for i in range(m):
            balls = [(x + abs(movement[x][y]), y + movement[x][y]) for x, y in balls]

        answer = []
        for x, y in balls:
            if x == m:
                answer.append(y)
            else:
                answer.append(-1)

        return answer

a = Solution()
print(a.findBall([[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1],[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1]]
))