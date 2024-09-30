from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isEvenOddTree(self, root: TreeNode) -> bool:
        level = 0
        deq = deque()
        deq.append(root)
        while len(deq) > 0:
            nextDeq = deque()
            temp = 987654321 if level % 2 else -1
            for i in range(len(deq)):
                if deq[i] == None:
                    continue

                if (level % 2 == 1) and (temp <= deq[i].val or deq[i].val % 2 == 1) \
                or (level % 2 == 0) and (temp >= deq[i].val or deq[i].val % 2 == 0):
                    return False

                temp = deq[i].val
                nextDeq.append(deq[i].left)
                nextDeq.append(deq[i].right)
            level += 1
            deq = nextDeq

        return True

                 
