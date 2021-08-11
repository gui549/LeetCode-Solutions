class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        que = []
        que.append(root)
        ans = 0
        while(True):
            s = 0
            nextQue = []
            while que:
                node = que.pop(0)
                if node.val == None:
                    continue
                s += node.val
                nextQue.append(node.left)
                nextQue.append(node.right)
            if not nextQue:
                return ans
            que = nextQue
            ans = s
            