from collections import deque

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        deq, copies = deque(), dict()
        if not node: 
            return None
    
        copies[node.val] = Node(node.val)
        deq.append(node)
        while deq:
            current = deq.popleft()
            for n in current.neighbors:
                if n.val not in copies:
                    copies[n.val] = Node(n.val)
                    deq.append(n)
                copies[current.val].neighbors.append(copies[n.val])

        return copies[node.val]
           

