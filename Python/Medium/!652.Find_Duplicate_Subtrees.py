from typing import List, Optional
from collections import defaultdict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        memo = defaultdict(list)
        def serialize(node):
            if node == None:
                return "#"
            serial = str(node.val) + serialize(node.left) + serialize(node.right)
            memo[serial].append(node)
            return serial

        serialize(root)
        return [memo[serial][0] for serial in memo if len(memo[serial]) > 1]