from typing import List
from collections import Counter

class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = Counter(nums1)
        self.nums2 = nums2
        self.cache = Counter(nums2)

    def add(self, index: int, val: int) -> None:
        self.cache[self.nums2[index]] -= 1
        self.nums2[index] += val
        self.cache[self.nums2[index]] += 1

    def count(self, tot: int) -> int:
        return sum(self.cache[tot - num1] * self.nums1[num1] for num1 in self.nums1)
    