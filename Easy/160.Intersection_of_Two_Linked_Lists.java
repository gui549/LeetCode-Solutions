package Easy;

import java.util.HashSet;

class ListNode {
    int val;
    ListNode next;
    ListNode(int x) {
        val = x;
        next = null;
    }
}

// memory O(1)
class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
		if (headA == null || headB == null)
			return null;
		
		ListNode currA = headA, currB = headB;
		while (currA != currB) {
			currA = currA == null ? headB : currA.next;
			currB = currB == null ? headA : currB.next;
		}
		return currA;
    }
}


// first solution
// class Solution {
//     public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
//         HashSet<ListNode> set = new HashSet<>();

//         while (headA != null) {
//             set.add(headA);
//             headA = headA.next;
//         }

//         while (headB != null) {
//             if (set.contains(headB)) return headB;
//             headB = headB.next;
//         }

//         return null;
//     }
// }