from typing import List

class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)
        cache = set()
        for i in range(n):
            visited = set()
            index = (i + nums[i]) % n
            while True:
                if ((nums[i] > 0) != (nums[index] > 0)) or (index in cache):
                    break
                
                if index in visited:
                    if nums[index] % n:
                        return True
                    else:
                        break
                
                visited.add(index)
                index = (index + nums[index]) % n
            cache = cache.union(visited)
        
        return False

a = Solution()
a.circularArrayLoop([1,1,2])
