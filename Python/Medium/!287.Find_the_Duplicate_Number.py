from typing import List

# Floyd's Tortoise and Hare Algorithm
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = nums[0], nums[nums[0]]
        while slow != fast: # Find a meeting point
            slow = nums[slow]
            fast = nums[nums[fast]]

        fast = 0
        while slow != fast: # Find a start point of the loop
            slow = nums[slow]
            fast = nums[fast]
        
        return slow