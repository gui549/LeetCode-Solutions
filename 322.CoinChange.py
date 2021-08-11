from collections import defaultdict
from typing import NewType

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        self.c = defaultdict(lambda: -1)
        count = self.recursion(coins, amount)
        if count == 9999:
            return -1
        return count

    def recursion(self, coins, amount):
        if amount == 0:
            return 0
        elif amount > 0:
            if self.c[amount] == -1:
                count = 9999
                for n in coins:
                    count = min(count, self.recursion(coins, amount - n) + 1)
                self.c[amount] = count
                return count
            else:
                return self.c[amount]
        else:
            return 9999    
