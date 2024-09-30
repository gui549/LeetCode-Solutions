from typing import List
import heapq

class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        m, n = len(mat), len(mat[0])
        candidate = []
        visited = set()
        heapq.heappush(candidate, (sum(mat[r][0] for r in range(m)), [0] * m))
        while True:
            current_sum, indices = heapq.heappop(candidate)
            
            print(indices)
            key = tuple(indices)
            if key in visited:
                continue

            if k == 1:
                return current_sum
            
            visited.add(key)
            for r, index in enumerate(indices):
                if index + 1 < n:
                    heapq.heappush(candidate, 
                                    (current_sum - mat[r][index] + mat[r][index + 1],
                                    indices[:r] + [index + 1] + indices[r+1:]))
            
            k -= 1

a = Solution()
a.kthSmallest([[1,1,10],[2,2,9]],7)