package Medium;

import java.util.LinkedList;
import java.util.Queue;

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(int x) { val = x; }
}


// better solution
class Solution {
    public final TreeNode getTargetCopy(final TreeNode original, final TreeNode cloned, final TreeNode target) {
        if (original == null || original == target) {
            return cloned;
        }
        TreeNode res = getTargetCopy(original.left, cloned.left, target);
        if (res != null) {
            return res;
        }
        return getTargetCopy(original.right, cloned.right, target);
    }
}


// first solution
// class Solution {
//     public final TreeNode getTargetCopy(final TreeNode original, final TreeNode cloned, final TreeNode target) {
//         Queue<TreeNode> originalQueue = new LinkedList<>();
//         Queue<TreeNode> clonedQueue = new LinkedList<>();
//         originalQueue.add(original);
//         clonedQueue.add(cloned);

//         while (!originalQueue.isEmpty() && !clonedQueue.isEmpty()) {
//             int size = originalQueue.size();

//             for (int i = 0; i < size; i++) {
//                 TreeNode currOriginal = originalQueue.poll();
//                 TreeNode currCloned = clonedQueue.poll();

//                 if (currOriginal == target) {
//                     return currCloned;
//                 }
                
//                 if (currOriginal.left != null) {
//                     originalQueue.add(currOriginal.left);
//                     clonedQueue.add(currCloned.left);
//                 } 

//                 if (currOriginal.right != null) {
//                     originalQueue.add(currOriginal.right);
//                     clonedQueue.add(currCloned.right);
//                 } 
//             }
//         }

//         return null;
//     }
// }