class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        nodes = [i for i in range(len(edges) + 1)]
        def find(n):
            if nodes[n] == n:
                return n
            nodes[n] = find(nodes[n]) # for optimizaiton
            return nodes[n]

        def union(n, m):
            nodes[find(m)] = n

        for a, b in edges:
            if find(a) == find(b):
                return [a, b]
            else:
                union(a, b)
