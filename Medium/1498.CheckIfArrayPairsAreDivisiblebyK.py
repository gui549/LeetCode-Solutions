class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        counter = [0] * k
        for num in arr:
            counter[num % k] += 1

        l, r = 1, len(counter) - 1
        while l <= r:
            if l == r:
                return counter[l] % 2 == 0

            if counter[l] != counter[r]:
                return False
         
            l -= 1
            r -= 1
            
        return True