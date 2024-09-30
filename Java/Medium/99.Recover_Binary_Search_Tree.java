package Medium;

import java.util.Comparator;
import java.util.LinkedList;

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode() {}
    TreeNode(int val) { this.val = val; }
    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

// Better Solution
class Solution {

    TreeNode firstNode, secondNode, prevNode;

    public void recoverTree(TreeNode root) {
        inOrder(root);

        int tmp = firstNode.val;
        firstNode.val = secondNode.val;
        secondNode.val = tmp;
    }

    public void inOrder(TreeNode root) {
        if (root == null) return;
        inOrder(root.left);

        if (firstNode == null && prevNode != null && prevNode.val >= root.val)
            firstNode = prevNode;
        
        if (firstNode != null && prevNode.val >= root.val) 
            secondNode = root;
        
        prevNode = root;

        inOrder(root.right);
    }
}

// class Solution {

//     LinkedList<TreeNode> nodes = new LinkedList<>();

//     public void recoverTree(TreeNode root) {
//         inOrder(root);
//         nodes.forEach((node) -> System.out.print(node.val + " "));
//         LinkedList<TreeNode> sortedNodes = new LinkedList<>(nodes);
//         sortedNodes.sort(new NodeComparator());
//         int firstIdx = -1, secondIdx = -1;
//         for (int i = 0; i < nodes.size(); i++) {
//             if (nodes.get(i).val != sortedNodes.get(i).val) {
//                 if (firstIdx == -1) {
//                     firstIdx = i;
//                 } else {
//                     secondIdx = i;
//                     break;
//                 } 
//             }
//         }
//         swap(firstIdx, secondIdx);
//     }

//     public void swap(int idx1, int idx2) {
//         int tmp = nodes.get(idx1).val;
//         nodes.get(idx1).val = nodes.get(idx2).val;
//         nodes.get(idx2).val = tmp;
//     }

//     public void inOrder(TreeNode root) {
//         if (root == null) return;
//         inOrder(root.left);
//         nodes.add(root);
//         inOrder(root.right);
//     }
// }

// class NodeComparator implements Comparator<TreeNode> {

//     @Override
//     public int compare(TreeNode o1, TreeNode o2) {
//         if (o1.val > o2.val) {
//             return 1;
//         } else if (o1.val < o2.val) {
//             return -1;
//         } else {
//             return 0;
//         }
//     }
// }