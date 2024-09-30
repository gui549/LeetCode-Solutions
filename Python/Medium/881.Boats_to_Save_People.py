from typing import List

""" My Solution
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        ans = 0
        ctr = Counter(people)
        used = 0
        prefix = [0]
        for i in range(1, limit // 2 + 1):
            prefix.append(prefix[-1] + ctr[i])
        
        for w in sorted(ctr, reverse=True):
            if w <= limit // 2:
                break
            
            save = min(ctr[w], prefix[limit - w] - used)
            if ctr[w] > save:
                ans += ctr[w] - save
            ans += save
            used += save
        
        ans += (prefix[-1] - used + 1) // 2
        return ans
"""

""" Better Solution """
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort(reverse=True)
        l, r = 0, len(people) - 1
        while l <= r:
            if people[l] + people[r] <= limit: r -= 1
            l += 1
        return l