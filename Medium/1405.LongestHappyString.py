import heapq

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        ans, heap = "", []
        heap = [heapq.heappush(heap, (count, char)) for count, char in [(-a, 'a'), (-b, 'b'), (-c, 'c')]]
        while True:
            count, char = heapq.heappop(heap)
            if len(ans) > 0 and ans[-1] == char:
                
            else:
                if count <= -2:
                    ans += char * 2
                    heapq.heappush((-count + 2, char))
                else:
                    ans += char * 1


            if prev != order[0][0]: 
                if order[0][1] >= 2:
                    ans += order[0][0] * 2
                    order[0][1] -= 2
                else:
                    ans += order[0][0] * order[0][1]
                    order[0][1] = 0
                prev = order[0][0]

            else:
                if order[1][1] >= 1:
                    ans += order[1][0]
                    order[1][1] -= 1
                    prev = order[1][0]
                else:
                    break

            order = sorted(order, key=lambda x: -x[1])
        
        return ans

a = Solution()
print(a.longestDiverseString(4, 4, 3))