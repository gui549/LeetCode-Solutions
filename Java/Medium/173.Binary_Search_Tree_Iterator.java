package Medium;

import java.util.Stack;

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

class BSTIterator {

    Stack<TreeNode> stack = new Stack<>();

    public BSTIterator(TreeNode root) {
        while (root != null) {
            stack.add(root);
            root = root.left;
        }
    }
    
    public int next() {
        TreeNode res = stack.pop();
        TreeNode pt = res.right;
        while (pt != null) {
            stack.push(pt);
            pt = pt.left;
        }
        return res.val;
    }
    
    public boolean hasNext() {
        return !stack.isEmpty();
    }
}
