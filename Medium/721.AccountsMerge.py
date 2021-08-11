from collections import defaultdict, deque
from typing import AnyStr, List

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        cache = defaultdict(list)
        for a in accounts:
            cache[a[0]].append(set(a[1:]))
    
        answer = []
        for name, addrlist in cache.items(): #addrlist =[{'...', '...', ...}, {'...', '...', ...}]
            while len(addrlist) > 0:
                temp = addrlist.pop(0)
                unionSet = temp
                for addr in addrlist:
                    if addr & temp != set():
                        unionSet = unionSet | addr
                if temp == unionSet:
                    result = list(unionSet)
                    result.sort()
                    answer.append([name] + result)
                    addrlist = [addr for addr in addrlist if addr & temp == set()]
                else:
                    addrlist = [unionSet] + [addr for addr in addrlist if addr & temp == set()]
                
        return answer

a = Solution()
print(a.accountsMerge([["David","David0@m.co","David1@m.co"],["David","David3@m.co","David4@m.co"],["David","David4@m.co","David5@m.co"],["David","David2@m.co","David3@m.co"],["David","David1@m.co","David2@m.co"]]))