from typing import List

class Solution:
    def checkMove(self, board: List[List[str]], rMove: int, cMove: int, color: str) -> bool:
        movement = [(1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1)]
        for dx, dy in movement:
            x, y, length = rMove, cMove, 1
            while 0 <= x + dx < 8 and 0 <= y + dy < 8:
                x, y = x + dx, y + dy
                length += 1
                if board[x][y] == '.' or (length < 3 and board[x][y] == color): break
                if board[x][y] == color:
                    return True
                
        return False
