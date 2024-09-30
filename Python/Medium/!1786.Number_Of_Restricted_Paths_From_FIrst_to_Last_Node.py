from functools import lru_cache
from typing import List
from collections import defaultdict
import heapq

class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        edge = defaultdict(dict)
        for u, v, weight in edges:
            edge[u - 1][v - 1] = weight
            edge[v - 1][u - 1] = weight

        min_dist = [1e10] * (n - 1) + [0] 
        heap = [(0, n - 1)]
        while heap:
            weight, node = heapq.heappop(heap)
            if min_dist[node] != weight:
                continue
            
            for adj_node in edge[node]:
                if min_dist[adj_node] > edge[node][adj_node] + weight:
                    min_dist[adj_node] = edge[node][adj_node] + weight
                    heapq.heappush(heap, (min_dist[adj_node], adj_node))

        @lru_cache(None)
        def recursive(node):
            if node == n - 1:
                return 1
            
            res = 0
            for adj_node in edge[node]:
                if min_dist[adj_node] < min_dist[node]:
                    res = (res + recursive(adj_node)) % 1000000007
            
            return res

        return recursive(0)
