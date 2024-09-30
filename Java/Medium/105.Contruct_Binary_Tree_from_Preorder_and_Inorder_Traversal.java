package Medium;

import java.util.Arrays;

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

// better solution
class Solution {

    int preorderIdx = 0;
    int inorderIdx = 0;

    public TreeNode buildTree(int[] preorder, int[] inorder) {
        return buildTree(preorder, inorder, Integer.MIN_VALUE);
    }

    public TreeNode buildTree(int[] preorder, int[] inorder, int stop) {
        if (inorderIdx >= inorder.length || inorder[inorderIdx] == stop)
            return null;

        TreeNode root = new TreeNode(preorder[preorderIdx++]);
        root.left = buildTree(preorder, inorder, root.val);
        inorderIdx++;
        root.right = buildTree(preorder, inorder, stop);
        return root;
    }
}


// first solution
// class Solution {

//     public TreeNode buildTree(int[] preorder, int[] inorder) {
//         if (preorder == null || inorder == null || preorder.length == 0 || inorder.length == 0) 
//             return null;
  
//         int rootIndex = -1;
//         for (int i = 0; i < inorder.length; i++) {
//             if (inorder[i] == preorder[0]) {
//                 rootIndex = i;
//             }
//         }           

//         if (rootIndex == -1) 
//             System.out.println("Something went wrong...");
        
//         TreeNode left = buildTree(Arrays.copyOfRange(preorder, 1, rootIndex + 1), 
//                                   Arrays.copyOfRange(inorder, 0, rootIndex));
//         TreeNode right = buildTree(Arrays.copyOfRange(preorder, rootIndex + 1, preorder.length), 
//                                    Arrays.copyOfRange(inorder, rootIndex + 1, preorder.length));
//         return new TreeNode(preorder[0], left, right);
//     }
// }