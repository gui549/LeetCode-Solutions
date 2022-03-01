from typing import List

class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans, exists = [], set()

        def recursive(index, current_sequence):
            if len(current_sequence) >= 2 and tuple(current_sequence) not in exists: # 
                ans.append(current_sequence)
                exists.add(tuple(current_sequence))
                
            if index >= len(nums):
                return
            
            if not current_sequence or current_sequence[-1] <= nums[index]:
                recursive(index + 1, current_sequence + [nums[index]])
            
            recursive(index + 1, current_sequence)

        recursive(0, [])
        return ans