from typing import List

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        m, n = len(board), len(board[0])
        neighbors = [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]
        for i in range(m):
            for j in range(n):
                temp = [board[i + dx][j + dy] for dx, dy in neighbors if 0 <= i + dx < m and 0 <= j + dy < n]
                print(temp)
                lives = temp.count(1) + temp.count(2)
                if board[i][j]:
                    if lives < 2 or lives > 3:
                        board[i][j] = 2
                    else:
                        board[i][j] = 1

                else:
                    if lives == 3:
                        board[i][j] = 3
                    else:
                        board[i][j] = 0
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 2:
                    board[i][j] = 0
                elif board[i][j] == 3:
                    board[i][j] = 1
        

a = Solution()
a.gameOfLife([[0,1,0],[0,0,1],[1,1,1],[0,0,0]])