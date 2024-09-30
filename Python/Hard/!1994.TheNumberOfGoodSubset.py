from typing import List
from functools import lru_cache
from collections import Counter

# From: https://leetcode.com/problems/the-number-of-good-subsets/discuss/1444338/python-dp-on-subsets-explained
class Solution:
    def numberOfGoodSubsets(self, nums: List[int]) -> int:
        P = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        cnt = Counter(nums)
        bm = [sum(1<<i for i, p in enumerate(P) if x % p == 0) for x in range(31)]
        bad = set([4, 8, 9, 12, 16, 18, 20, 24, 25, 27, 28])
        M = 10**9 + 7

        print(bm)
        @lru_cache(None)
        def dp(mask, num):
            if num == 1: return 1
            ans = dp(mask, num - 1)
            if num not in bad and mask | bm[num] == mask:
                ans += dp(mask ^ bm[num], num - 1) * cnt[num]
            return ans % M

        return ((dp(1023, 30) - 1) * pow(2, cnt[1], M)) % M

s = Solution()
s.numberOfGoodSubsets([11,2,13,24,11,2,1,12,3,14,1])