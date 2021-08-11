class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        a, b = 0, n
        if left:
            a = max(left)
    
        if right:
            b = min(right)
        
        return max(a, n - b)


