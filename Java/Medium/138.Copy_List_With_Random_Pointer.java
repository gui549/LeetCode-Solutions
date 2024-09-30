package Medium;

import java.util.HashMap;

class Node {
    int val;
    Node next;
    Node random;

    public Node(int val) {
        this.val = val;
        this.next = null;
        this.random = null;
    }
}

// advanced solution
class Solution {
    public Node copyRandomList(Node head) {
        Node iter = head, next;

        while (iter != null) {
            next = iter.next;

            Node copy = new Node(iter.val);
            iter.next = copy;
            copy.next = next;

            iter = next;
        }

        iter = head;
        while (iter != null) {
            if (iter.random != null) {
                iter.next.random = iter.random.next;
            }
            iter = iter.next.next;
        }

        iter = head;
        Node copyHead = new Node(0);
        Node copy, copyIter = copyHead;
        while (iter != null) {
            next = iter.next.next;

            copy = iter.next;
            copyIter.next = copy;
            copyIter = copy;

            iter.next = next;

            iter = next;
        }
        return copyHead.next;
    } 
}



// better solution
// class Solution {
//     public Node copyRandomList(Node head) {
//         if (head == null) return null;

//         HashMap<Node, Node> map = new HashMap<Node, Node>();

//         Node node = head;
//         while (node != null) {
//             map.put(node, new Node(node.val));
//             node = node.next;
//         }

//         node = head;
//         while (node != null) {
//             map.get(node).next = map.get(node.next);
//             map.get(node).random = map.get(node.random);
//             node = node.next;
//         }

//         return map.get(head);
//     } 
// }


// fisrt solution
// class Solution {
//     public Node copyRandomList(Node head) {
//         HashMap<Node, Integer> oldNodeToIdx = new HashMap<>();
//         HashMap<Integer, Node> idxToNewNode = new HashMap<>();

//         int idx = 0;
//         Node root = new Node(0);
//         Node oldNode = head;
//         Node newNode = root;
//         while (oldNode != null) {
//             oldNodeToIdx.put(oldNode, idx);
//             newNode.next = new Node(oldNode.val);
//             idxToNewNode.put(idx, newNode.next);

//             idx++;
//             oldNode = oldNode.next;
//             newNode = newNode.next;
//         }

//         oldNode = head;
//         newNode = root;
//         while (oldNode != null) {
//             if (oldNode.random == null) {
//                 newNode.next.random = null;
//             } else {
//                 int randomIdx = oldNodeToIdx.get(oldNode.random);
//                 newNode.next.random = idxToNewNode.get(randomIdx);
//             }
//             oldNode = oldNode.next;
//             newNode = newNode.next;
//         }

//         return root.next;
//     }
// }