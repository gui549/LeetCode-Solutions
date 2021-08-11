class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        cache = {}
        def canWin(choice, desired):
            if choice and max(choice) >= desired:
                return True

            """ Must Know! """
            key = tuple(choice) 
            if key in cache:
                return cache[key]

            for i in range(len(choice)):
                if not canWin(choice[:i] + choice[i + 1:], desired - choice[i]):
                    cache[key] = True
                    return True

            cache[key] = False
            return False
        
        choices = [i for i in range(1, maxChoosableInteger + 1)]

        if sum(choices) < desiredTotal:
            return False

        elif sum(choices) == desiredTotal:
            return len(choices) % 2 == 1

        else:
            return canWin(choices, desiredTotal)