package Medium;

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
    public int kthSmallest(TreeNode root, int k) {
        LinkedList <TreeNode> stack = new LinkedList<>();

        while (true) {
            while (root != null) {
                stack.push(root);
                root = root.left;
            }
            root = stack.pop();
            if (--k == 0) return root.val;
            root = root.right;
        }
    }
}


// First Solution
// class Solution {

//     int count = 0;
    
//     public int kthSmallest(TreeNode root, int k) {
//         int tmp = -1;
//         if (root.left == null) {

//         }
//         if (root.left != null) {
//             tmp = kthSmallest(root.left, k);
//             if (tmp != -1) return tmp;
//         }

//         if (++count == k) return root.val;

//         if (root.right != null) {
//             return kthSmallest(root.right, k);
//         }

//         return tmp;
//     }
// }