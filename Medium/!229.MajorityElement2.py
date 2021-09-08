from typing import List
from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counter = Counter()
        for n in nums:
            counter[n] += 1
            if len(counter) == 3:
                # set(counter) => {counter.keys()}
                # Counter({set}) => {"all keys": 1}
                # counter -= counter => if value == 0, then delete key
                counter -= Counter(set(counter))
 
        return [key for key in counter if nums.count(key) > len(nums) / 3]
        
