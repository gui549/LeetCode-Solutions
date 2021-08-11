import math
import heapq
from typing import List  

from queue import PriorityQueue
from collections import defaultdict     

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        probs = defaultdict(list) 
        for i, edge in enumerate(edges):
            probs[edge[0]].append((edge[1], succProb[i]))
            probs[edge[1]].append((edge[0], succProb[i]))

        que = PriorityQueue()
        visited = defaultdict(bool)
        que.put((-1.0, start))
        while not que.empty():
            prob, node = que.get()
            if node == end:
                return -prob
            
            visited[node] = True
            for reachNode, reachProb in (probs[node]):
                if not visited[reachNode]:
                     que.put((prob * reachProb, reachNode))

        return 0.0

a = Solution()
print(a.maxProbability(5,[[1,4],[2,4],[0,4],[0,3],[0,2],[2,3]],[0.37,0.17,0.93,0.23,0.39,0.04],3,4))
print(a.maxProbability(3,[[0,1]],[0.5],0,2))
print(a.maxProbability(3,[[0,1],[1,2],[0,2]],[0.5,0.5,0.2],0,2))
print(a.maxProbability(3,[[0,1],[1,2],[0,2]],[0.5,0.5,0.3],0,2))
print(a.maxProbability(5,[[2,3],[1,2],[3,4],[1,3],[1,4],[0,1],[2,4],[0,4],[0,2]],[0.06,0.26,0.49,0.25,0.2,0.64,0.23,0.21,0.77],0,3))

