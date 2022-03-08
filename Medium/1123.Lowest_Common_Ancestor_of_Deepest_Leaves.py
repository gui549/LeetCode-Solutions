from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        que = deque([(root, 0)])
        ans, max_depth = root, 0
        while que:
            node, depth = que.pop()
            if node.left or node.right:
                if max_depth < depth:
                    ans = node
                    max_depth = depth

            if node.left:
                que.append((node.left, depth + 1))

            if node.right:
                que.append((node.))
            