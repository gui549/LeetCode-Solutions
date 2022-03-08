from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def recursive(node):
            if not node:
                return 0, None
            
            left_depth, left_node = recursive(node.left)
            right_depth, right_node = recursive(node.right)
            
            if left_depth > right_depth: 
                return left_depth + 1, left_node
            
            if left_depth < right_depth:
                return right_depth + 1, right_node

            return left_depth + 1, node
        return recursive(root)[1]