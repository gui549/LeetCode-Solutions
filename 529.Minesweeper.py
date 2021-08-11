from typing import List
from collections import deque

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        m, n = len(board), len(board[0])
        neighbors = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
        deq = deque()
        def check(x, y):
            if board[x][y] == 'M':
                board[x][y] = 'X'
                return

            elif board[x][y] == 'E':
                count = 0
                next = []
                for dx, dy in neighbors:
                    if x + dx < 0 or x + dx >= m or y + dy < 0 or y + dy >= n:
                        continue
                    
                    if board[x + dx][y + dy] == 'M':
                        count += 1
                    else:
                        next.append([x + dx, y + dy])
                        
                if count > 0:
                    board[x][y] = str(count)
                else:
                    board[x][y] = 'B'
                    [deq.append([newX, newY]) for newX, newY in next]
        

        deq.append(click)
        while deq:
            # print(deq)
            newX, newY = deq.popleft()
            check(newX, newY)

        return board


a = Solution()
a.updateBoard([["E","E","E","E","E"],["E","E","M","E","E"],["E","E","E","E","E"],["E","E","E","E","E"]],[3,0])