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
    public boolean isSymmetric(TreeNode root) {
        return isSymmetric(root.left, root.right);
    }

    private boolean isSymmetric(TreeNode left, TreeNode right) {
        if (left == null && right == null) return true;
        if (left == null || right == null) return false; // ✅
        return (left.val == right.val) && isSymmetric(left.right, right.left) 
                                       && isSymmetric(left.left, right.right);
    }
}

// solve iteratively
// class Solution {
//     public boolean isSymmetric(TreeNode root) {
//         Queue<TreeNode> queue = new LinkedList<>();

//         queue.add(root.left);
//         queue.add(root.right);
        
//         while (queue.size() > 1) {
//             TreeNode leftNode = queue.poll();
//             TreeNode rightNode = queue.poll();

//             if (leftNode == null && rightNode == null)
//                 continue;
            
//             if (leftNode == null || rightNode == null)
//                 return false;

//             if (leftNode.val != rightNode.val)
//                 return false;
            
//             queue.add(leftNode.left);
//             queue.add(rightNode.right);
//             queue.add(leftNode.right);
//             queue.add(rightNode.left);
//         }

//         return true;
//     }
// }