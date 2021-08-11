from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# My Solution 
# class Solution:
#     def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         def lastNode(node):
#             while node.next:
#                 node = node.next
#             return node

#         def select_pivot(node):
#             i, j, k = node, node, node
#             while k and k.next:
#                 j = j.next
#                 k = k.next.next

#             temp = i.val
#             i.val = j.val
#             j.val = temp
#             return node
        
#         def quicksort(node):
#             if node is None:
#                 return
            
#             pivot = select_pivot(node)
#             successor = pivot
#             front, rear = ListNode(), ListNode()
#             fp, rp, pp = front, rear, pivot
#             while successor.next:
#                 successor = successor.next
#                 if successor.val < pivot.val:
#                     fp.next = ListNode(successor.val)
#                     fp = fp.next
#                 elif successor.val > pivot.val: 
#                     rp.next = ListNode(successor.val)
#                     rp = rp.next
#                 else:
#                     pp.next = ListNode(successor.val)
#                     pp = pp.next

#             front = quicksort(front.next)
#             if front is None:
#                 pp.next = quicksort(rear.next)
#                 return pivot
            
#             pp.next = quicksort(rear.next)
#             lastNode(front).next = pivot    
#             return front

#         return quicksort(head)

# Refer to https://leetcode.com/problems/sort-list/discuss/46827/Python-quick-sort-solution-easy-to-understand-beats-95.51
class Solution(object):
    def sortList(self, head):
        def partition(start, end):
            node = start.next.next
            pivotPrev = start.next
            pivotPrev.next = end
            pivotPost = pivotPrev
            while node != end:
                temp = node.next
                if node.val > pivotPrev.val:
                    node.next = pivotPost.next
                    pivotPost.next = node
                elif node.val < pivotPrev.val:
                    node.next = start.next
                    start.next = node
                else:
                    node.next = pivotPost.next
                    pivotPost.next = node
                    pivotPost = pivotPost.next
                node = temp
            return [pivotPrev, pivotPost]
        
        def quicksort(start, end):
            if start.next != end:
                prev, post = partition(start, end)
                quicksort(start, prev)
                quicksort(post, end)

        newHead = ListNode(0)
        newHead.next = head
        quicksort(newHead, None)
        return newHead.next

a = Solution()
li = [-1,5,3,4,0, 10, 2, -5, 20, 15]
ptr = None
for i in li[::-1]:
    ptr = ListNode(i, ptr)

a.sortList(ptr)