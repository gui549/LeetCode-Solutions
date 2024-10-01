package Medium;

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

class Solution {
    
    private int sum = 0;

    public TreeNode convertBST(TreeNode root) {
        if (root == null) return null;
        if (root.right != null) {
            convertBST(root.right);
        }

        sum += root.val;
        root.val = sum;
        if (root.left != null) {
            convertBST(root.left);
        }

        return root;
    }
}