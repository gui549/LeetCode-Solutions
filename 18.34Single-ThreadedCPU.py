from typing import List
from collections import defaultdict, deque
import heapq

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        ans, time = [], 0
        series = defaultdict(list)
        for i, (enqueTime, procTime) in enumerate(tasks):
            series[enqueTime].append((procTime, i))
        keys = deque(sorted(series.keys()))
        
        waiting = []
        while len(ans) < len(tasks):
            while keys and time >= keys[0]:
                [heapq.heappush(waiting, tup) for tup in series[keys.popleft()]]
            
            if waiting:
                procTime, index = heapq.heappop(waiting)
                ans.append(index)
                time += procTime
            
            else:
                time = keys[0]

        return ans

a = Solution()
print(a.getOrder([[19,13],[16,9],[21,10],[32,25],[37,4],[49,24],[2,15],[38,41],[37,34],[33,6],[45,4],[18,18],[46,39],[12,24]]))