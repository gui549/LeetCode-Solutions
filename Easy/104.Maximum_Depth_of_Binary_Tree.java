package Easy;

import java.util.LinkedList;
import java.util.Queue;

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

// solve recursively
class Solution {
    public int maxDepth(TreeNode root) {
        if (root == null) return 0;

        return 1 + Math.max(maxDepth(root.left), maxDepth(root.right));
    }
}


// solve iteratively
// class Solution {
//     public int maxDepth(TreeNode root) {
//         int depth = 0;
//         if (root == null) return depth;

//         Queue<TreeNode> queue = new LinkedList<>();
//         queue.add(root);
        
//         while(!queue.isEmpty()) {
//             depth++;
//             int numNodes = queue.size();
//             for (int i = 0; i < numNodes; i++) {
//                 TreeNode node = queue.poll();
//                 if (node.left != null) queue.add(node.left);
//                 if (node.right != null) queue.add(node.right);
//             }
//         }
//         return depth;
//     }
// }