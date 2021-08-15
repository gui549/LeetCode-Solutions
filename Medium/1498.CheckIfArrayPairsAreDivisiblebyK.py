from collections import deque

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        counter = deque([0] * k)
        for num in arr:
            counter[num % k] += 1

        counter.popleft()
        while len(counter) > 1:
            if counter.popleft() != counter.pop():
                return False
        
        if len(counter) == 1 and counter.pop() % 2:
            return False

        return True