from collections import Counter
from typing import List
import heapq

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        ctr = Counter(words)
        ctr = [(-v, k) for k, v in ctr.items()]
        heapq.heapify(ctr)
        return [heapq.heappop(ctr)[1] for _ in range(k)]