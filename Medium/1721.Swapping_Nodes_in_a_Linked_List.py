from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        slow = fast = ans = head
        for i in range(k - 1):
            head = head.next
            fast = fast.next

        while fast.next is not None:
            fast = fast.next
            slow = slow.next

        head.val, slow.val = slow.val, head.val
        return ans
                