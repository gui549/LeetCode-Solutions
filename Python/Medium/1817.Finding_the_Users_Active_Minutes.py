from collections import defaultdict, Counter
from typing import List


class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        user_minutes = defaultdict(set)
        for id, time in logs:
            user_minutes[id].add(time)

        ctr = Counter()
        for id in user_minutes:
            ctr[len(user_minutes[id])] += 1

        return [ctr[i] for i in range(1, k+1)]