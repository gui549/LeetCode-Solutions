from typing import List

#
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res, ans = [], []
        queens = [-1] * n
        def dfs(index):
            if index == n:
                res.append(queens.copy())
                return
            for i in range(n):
                queens[index] = i
                if valid(index):
                    dfs(index + 1)

        def valid(index):
            for i in range(index):
                if queens[i] == queens[index]:
                    return False
                
                if abs(queens[index] - queens[i]) == index - i:
                    return False
            return True

        dfs(0)
        print(res)
        for indices in res:
            chess = [['.'] * n for _ in range(n)]
            for r, c in enumerate(indices):
                chess[r][c] = 'Q'
            ans.append([("".join(row)) for row in chess])

        return ans


# Brute Force
# class Solution:
#     def solveNQueens(self, n: int) -> List[List[str]]:
#         movement = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)] 
#         ans = []
#         def translate(num):
#             return num // n, num % n
        
#         def set_queen(chess, last, count):
#             if count == n:
#                 return ans.append([("".join(row)).replace('*', '.', n) for row in chess])
            
#             for next in range(last, n ** 2):
#                 i, j = translate(next)
#                 if chess[i][j] == '.':
#                     newChess = [row[:] for row in chess]
#                     newChess[i][j] = 'Q'
#                     for dx, dy in movement:
#                         x, y = i + dx, j + dy
#                         while 0 <= x < n and 0 <= y < n:
#                             if newChess[x][y] == '.':
#                                 newChess[x][y] = '*'
#                             x, y = x + dx, y + dy

#                     set_queen(newChess, next + 1, count + 1)

#         chess = [['.'] * n for _ in range(n)]
#         set_queen(chess, 0, 0)

#         return ans

a = Solution()
print(a.solveNQueens(9))