class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        freind = [-1] * n
        for a, b in pairs:
            freind[a] = b
            freind[b] = a

        cnt = 0
        for i in range(n):
            pair = freind[i]
            find = False
            for j in preferences[i]:
                if j == pair:
                    break
                if not find:
                    for k in preferences[j]:
                        if k == i:
                            cnt +=1
                            find = True
                            break
                        if k == freind[j]:
                            break
                else:
                    break
        
        return cnt
                

