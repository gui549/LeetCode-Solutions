from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        changed = False
        i = len(nums) - 1
        while not changed and 0 <= i :
            for j in range(len(nums) - 1, i, -1):
                if nums[i] < nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
                    changed = True
                    break
            if not changed: i -= 1
        
        for j in range(len(nums) - i - 1):
            for k in range(i + 1, len(nums) - j):
                if nums[k] > nums[k + 1]:
                    nums[k], nums[k + 1] = nums[k + 1], nums[k]

s = Solution()
s.nextPermutation([1])