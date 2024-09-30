from collections import defaultdict
from typing import List

class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for m, n in adjacentPairs:
            graph[m].append(n)
            graph[n].append(m)

        ans = []
        seen = set()
        que = [next(m for m in graph if len(graph[m]) == 1)]
        while que:
            m = que.pop()
            for n in graph[m]:
                if n in seen:
                    continue
                que.append(n)
            
            seen.add(m)
            ans.append(m)

        return ans