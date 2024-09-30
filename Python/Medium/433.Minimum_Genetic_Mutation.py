from typing import List
from collections import deque

class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        que, visited = deque([(start, 0)]), set()
        while que:
            current_gene, num_mutations = que.popleft()

            if current_gene == end:
                return num_mutations

            if current_gene in visited:
                continue

            visited.add(current_gene)
            for valid_gene in bank:
                count = sum([c != v for c, v in zip(current_gene, valid_gene)])
                if count == 1:
                    que.append((valid_gene, num_mutations + 1))
                
        return -1 
            
