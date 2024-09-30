package Medium;

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

class Solution {
    public Node connect(Node root) {
        Node firstNodeOnLevel = root;
        while (firstNodeOnLevel != null) {
            Node currNode = firstNodeOnLevel, firstNodeOnNextLevel = null, currChild = null;
            while (currNode != null) {
                if (currNode.left != null) {
                    if (currChild == null) {
                        currChild = currNode.left;
                        firstNodeOnNextLevel = currChild;
                    } else {
                        currChild.next = currNode.left;
                        currChild = currChild.next;
                    }
                }
                if (currNode.right != null) {
                    if (currChild == null) {
                        currChild = currNode.right;
                        firstNodeOnNextLevel = currChild;
                    } else {
                        currChild.next = currNode.right;
                        currChild = currChild.next;
                    }
                }
                currNode = currNode.next;
            }
            firstNodeOnLevel = firstNodeOnNextLevel;
        }
        return root;
    }
}