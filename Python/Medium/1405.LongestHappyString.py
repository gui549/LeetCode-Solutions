import heapq

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        ans, heap = "", []
        [heapq.heappush(heap, (count, char)) for count, char in [(-a, 'a'), (-b, 'b'), (-c, 'c')] if count]
        while heap:
            count, char = heapq.heappop(heap)
            if len(ans) > 0 and ans[-1] == char:
                if not heap: 
                    break
                count, char = heapq.heapreplace(heap, (count, char))
                ans += char
                if count + 1: 
                    heapq.heappush(heap, (count + 1, char))

            else:
                if count <= -2:
                    ans += char * 2
                    if count < -2: heapq.heappush(heap, (count + 2, char))
                else:
                    ans += char * 1

        return ans

a = Solution()
print(a.longestDiverseString(4, 4, 3))