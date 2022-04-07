from typing import List
import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            y, x = -heapq.heappop(stones), -heapq.heappop(stones)
            if y - x:
                heapq.heappush(stones, -y + x)
        
        return -stones.pop() if stones else 0