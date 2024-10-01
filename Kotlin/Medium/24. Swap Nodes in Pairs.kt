/**
 * Example:
 * var li = ListNode(5)
 * var v = li.`val`
 * Definition for singly-linked list.
 * class ListNode(var `val`: Int) {
 *     var next: ListNode? = null
 * }
 */
class Solution {
    fun swapPairs(head: ListNode?): ListNode? {
        if (head == null || head.next == null) {
            return head
        }

        val result: ListNode = ListNode()

        var previous = result
        var first = head
        while (first != null) {
            if (first.next == null) {
                previous.next = first
                break;
            }

            val second = first.next
            val nextFirst = second.next
            second.next = first
            first.next = nextFirst
           
            previous.next = second
            previous = first
            first = nextFirst
        }

        return result.next;
    }
}