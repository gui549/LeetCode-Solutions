from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def recursion(n1, n2, carrier):
            value = carrier
            if n1 is None and n2 is None and not value:
                return None

            if n1 is not None:
                value += n1.val
                n1 = n1.next

            if n2 is not None:
                value += n2.val
                n2 = n2.next

            return ListNode(value % 10, recursion(n1, n2, value // 10))

        return recursion(l1, l2, 0)

