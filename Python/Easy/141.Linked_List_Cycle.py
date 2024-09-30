from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# better solution
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        try:
            slow = head
            fast = head.next
            while slow is not fast:
                slow = slow.next
                fast = fast.next.next
            return True
        except:
            return False

# first solution
# class Solution:
#     def hasCycle(self, head: Optional[ListNode]) -> bool:
#         if head == None or head.next == None or head.next.next == None:
#             return False
#         slow = head.next
#         fast = head.next.next
#         while (slow != fast):
#             if slow.next == None: 
#                 return False

#             if fast.next == None or fast.next.next == None: 
#                 return False

#             slow = slow.next
#             fast = fast.next.next
    

#         return True