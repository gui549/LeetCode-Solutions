package Easy;

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

    public TreeNode increasingBST(TreeNode root) {
        return increasingBST(root, null);
    }

    public TreeNode increasingBST(TreeNode root, TreeNode tail) {
        if (root == null) return tail;
        TreeNode res = increasingBST(root.left, root);
        root.left = null;
        root.right = increasingBST(root.right, tail);
        return res;
    }
}


// First Solution
// class Solution {

//     public TreeNode increasingBST(TreeNode root) {
//         TreeNode head = new TreeNode();
//         increasingBST(head, root);
//         return head.right;
//     }

//     public void increasingBST(TreeNode head, TreeNode currNode) {
//         if (currNode == null) return;
//         if (currNode.left != null) increasingBST(head, currNode.left);
//         while (head.right != null) {
//             head = head.right;
//         }        
//         head.right = new TreeNode(currNode.val);
//         if (currNode.right != null) increasingBST(head, currNode.right);
//     }
// }