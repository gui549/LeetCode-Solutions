from typing import List

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        li = []
        
        # Sort x[0] in desc and x[1] in asc
        people = sorted(people, key=lambda x: (-x[0], x[1]))
        
        for p in people:
            li.insert(p[1], p)
        
        return li

a = Solution()
print(a.reconstructQueue([[7, 1], [7,0],[4,4],[5,0],[6,1],[5,2]]))
