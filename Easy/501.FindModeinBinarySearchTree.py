from typing import Optional, List
from collections import Counter, deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        counter = Counter()
        deq = deque([root])
        while deq:
            node = deq.popleft()
            counter[node.val] += 1
            if node.left:
                deq.append(node.left)
            
            if node.right:
                deq.append(node.right)

        max_count = max(counter.values())
        return [value for value, count in counter.items() if count == max_count]
        
a = Solution()
a.findMode(TreeNode(0))
