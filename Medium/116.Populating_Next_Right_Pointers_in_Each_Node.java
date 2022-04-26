package Medium;

import java.util.LinkedList;
import java.util.Queue;

class Node {
    public int val;
    public Node left;
    public Node right;
    public Node next;

    public Node() {}
    
    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, Node _left, Node _right, Node _next) {
        val = _val;
        left = _left;
        right = _right;
        next = _next;
    }
};


// better solution
class Solution {
    public Node connect(Node root) {
        Node startNodeOnLevel = root;
        while (startNodeOnLevel != null) {
            Node currentNode = startNodeOnLevel;
            while (currentNode != null) {
                if (currentNode.left != null) 
                    currentNode.left.next = currentNode.right;
                if (currentNode.right != null && currentNode.next != null) 
                    currentNode.right.next = currentNode.next.left;
                currentNode = currentNode.next;
            }
            startNodeOnLevel = startNodeOnLevel.left;
        }
        return root;
    }
}


// first solution
// class Solution {
//     public Node connect(Node root) {
//         if (root == null) return root;
//         Queue<Node> queue = new LinkedList<>();
        
//         queue.add(root);
//         while(!queue.isEmpty()) {
//             int numNodes = queue.size();
//             Node prevNode = null;
//             for (int i = 0; i < numNodes; i++) {
//                 Node node = queue.poll();
//                 if (node.left != null) {
//                     queue.add(node.left);
//                     if (prevNode != null) prevNode.next = node.left;
//                     prevNode = node.left;
//                 }
//                 if (node.right != null) {
//                     queue.add(node.right);
//                     if (prevNode != null) prevNode.next = node.right;
//                     prevNode = node.right;
//                 }
//             }
//         }
//         return root;
//     }
// }