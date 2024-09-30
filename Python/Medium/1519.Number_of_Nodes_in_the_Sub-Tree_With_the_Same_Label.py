from collections import Counter
from typing import List


class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        ans = [0] * n
        graph = [[] for _ in range(n)]
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        def recursive(node, parent):
            res = Counter([labels[node]])
            for next_node in graph[node]:
                if next_node == parent:
                    continue
                
                res += recursive(next_node, node)
                
            ans[node] = res[labels[node]]
            return res

        recursive(0, None)
        return ans