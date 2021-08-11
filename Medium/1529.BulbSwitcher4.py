class Solution:
    def minFlips(self, target: str) -> int:
        count = 0
        t = '0'
        for c in target:
            if c != t:
                count += 1
                t = '0' if t == '1' else '1'
        
        return count
