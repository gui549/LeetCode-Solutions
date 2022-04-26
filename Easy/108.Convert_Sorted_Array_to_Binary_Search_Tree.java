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


class Solution {
    public TreeNode sortedArrayToBST(int[] nums) {
        return sortedArrayToBST(nums, 0, nums.length);
    }
    
    public TreeNode sortedArrayToBST(int[] nums, int left, int right) {
        if (left >= right) return null;
        int mid = left + (right - left) / 2;
        TreeNode leftNode = sortedArrayToBST(nums, left, mid);
        TreeNode rightNode = sortedArrayToBST(nums, mid + 1, right);
        
        return new TreeNode(nums[mid], leftNode, rightNode);

    }
}