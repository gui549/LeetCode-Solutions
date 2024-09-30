from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def check(x, y):
            for i in range(9):
                if i != x and board[x][y] == board[i][y] != '.':
                    return False
            
            for j in range(9):
                if j != y and board[x][y] == board[x][j] != '.':
                    return False
            
            for i in range(x - (x % 3), x - (x % 3) + 3):
                for j in range(y - (y % 3), y - (y % 3) + 3):
                    if x != i and y != j and board[x][y] == board[i][j] != '.':
                        return False

            return True

        for i in range(9):
            for j in range(9):
                if not check(i, j):
                    print(i, j)
                    return False
        return True
            