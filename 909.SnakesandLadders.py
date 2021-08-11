from typing import List
from collections import defaultdict

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        def translate(num):
            row, col = (num - 1) // n, (num - 1) % n
            return (~row, ~col if row % 2 else col)

        bfs, visited = [], defaultdict(bool)
        bfs.append((0, 1)) # (count, index)
        while bfs:
            c, i = bfs.pop(0)
            if i == n ** 2:
                return c 
            
            for j in range(i + 1, min(i + 7, n ** 2 + 1)):
                x, y = translate(j)
                if board[x][y] > 0: j = board[x][y]
                if not visited[j]: 
                    bfs.append((c + 1, j))
                    visited[j] = True
        
        return -1

a = Solution()
print(a.snakesAndLadders([[-1,-1,30,14,15,-1],[23,9,-1,-1,-1,9],[12,5,7,24,-1,30],[10,-1,-1,-1,25,17],[32,-1,28,-1,-1,32],[-1,-1,23,-1,13,19]]))
print(a.snakesAndLadders([[-1,-1,2,21,-1],[16,-1,24,-1,4],[2,3,-1,-1,-1],[-1,11,23,18,-1],[-1,-1,-1,23,-1]]))

