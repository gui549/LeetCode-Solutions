from typing import List
from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        requisite = defaultdict(list)
        cache = dict()
        for a, b in prerequisites:
            requisite[a].append(b)
        
        def recursion(course):
            if course in cache:
                return cache[course]
            
            cache[course] = False
            for precourse in requisite[course]:
                if not recursion(precourse): 
                    return cache[course]
            
            cache[course] = True
            return cache[course]

        return all([recursion(key) for key in requisite.copy()])

a = Solution()
a.canFinish(2, [[1, 0]])