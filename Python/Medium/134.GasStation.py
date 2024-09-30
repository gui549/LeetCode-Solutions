class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        i = 0
        while i < len(gas):
            if gas[i] < cost[i]:
                i += 1
                continue
       
            s = 0
            for j in range(i, i + len(gas)):
                s += gas[j % len(gas)] - cost[j % len(gas)]
                if s < 0:
                    i = j + 1
                    break
            
            if s >= 0:
                return i
            
