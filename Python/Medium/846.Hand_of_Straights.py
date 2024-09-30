from typing import Counter, List

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        ctr = Counter(hand)

        for num in sorted(ctr):
            freq = ctr[num]
            if freq:
                for i in range(groupSize):
                    if ctr[num + i] >= freq:
                        ctr[num + i] -= freq
                    else:
                        return False

        return True