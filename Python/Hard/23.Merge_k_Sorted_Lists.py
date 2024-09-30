import heapq
from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # ListNode.__eq__ = lambda self, other: self.val == other.val   # Pythonic
        # ListNode.__lt__ = lambda self, other: self.val < other.val    # Pythonic
        head = curr = ListNode(0, None)
        heap = [(li.val, idx) for idx, li in enumerate(lists) if li]
        heapq.heapify(heap)
        while heap:
            val, idx = heapq.heappop(heap)            
            li = lists[idx]
            curr.next = li
            curr = curr.next
            if li.next:
                lists[idx] = li.next
                heapq.heappush(heap, (li.next.val, idx))
                li.next = None

        return head.next
       

s = Solution()
s.mergeKLists([ListNode(3), ListNode(2, ListNode(4))])