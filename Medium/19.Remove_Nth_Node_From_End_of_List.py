from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Better Solution
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = fast = head
        for _ in range(n):
            fast = fast.next
        if fast is None:        # ❗
            return head.next
        while fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return head


""" First Solution
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr_node = head
        prev_node, target_node = None, head
        count = 1
        while curr_node is not None:
            if count < n:
                count += 1
            else:
                prev_node = target_node
                target_node = target_node.next
            curr_node = curr_node.next
        prev_node.next = target_node.next
        return head
"""