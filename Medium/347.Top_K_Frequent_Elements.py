from collections import Counter
import heapq
from itertools import chain
from typing import List

# Use bucket sort
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for _ in range(len(nums) + 1)]
        ctr = Counter(nums)
        for key, freq in ctr.items():
            buckets[freq].append(key)
        return list(chain(*buckets))[::-1][:k]


""" Use Heap
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ctr = Counter(nums)
        return heapq.nlargest(k, ctr.keys(), key=ctr.get)
"""


