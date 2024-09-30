package Medium;

import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Deque;
import java.util.LinkedList;
import java.util.List;

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

// Simpler Solution
class Solution {
    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        List<List<Integer>> ans = new ArrayList<>();
        if (root == null) return ans;
        
        Deque<TreeNode> deque = new ArrayDeque<>();
        deque.addLast(root);
        boolean isLeftToRight = false;

        while (!deque.isEmpty()) {
            int numNodes = deque.size();
            LinkedList<Integer> nodeValues = new LinkedList<>();
            for (int i = 0; i < numNodes; i++) {
                TreeNode node = deque.poll();
                if (isLeftToRight) {
                    nodeValues.addFirst(node.val);;
                } else {
                    nodeValues.add(node.val);
                }
                if (node.left != null) deque.add(node.left);
                if (node.right != null) deque.add(node.right);
            }
            ans.add(nodeValues);
            isLeftToRight = !isLeftToRight;
        }
        return ans;
    }
}

// First Solution
// class Solution {
//     public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
//         List<List<Integer>> ans = new ArrayList<>();
//         if (root == null) return ans;
        
//         Deque<TreeNode> deque = new ArrayDeque<>();
//         deque.addLast(root);
//         boolean isLeftToRight = false;

//         while (!deque.isEmpty()) {
//             int numNodes = deque.size();
//             List<Integer> nodeValues = new ArrayList<>();
//             for (int i = 0; i < numNodes; i++) {
//                 if (isLeftToRight) {
//                     TreeNode node = deque.pollLast();
//                     nodeValues.add(node.val);
//                     if (node.right != null) deque.addFirst(node.right);
//                     if (node.left != null) deque.addFirst(node.left);
//                 } else {
//                     TreeNode node = deque.pollFirst();
//                     nodeValues.add(node.val);
//                     if (node.left != null) deque.addLast(node.left);
//                     if (node.right != null) deque.addLast(node.right);
//                 }
//             }
//             ans.add(nodeValues);
//             isLeftToRight = !isLeftToRight;
//         }
//         return ans;
//     }
// }