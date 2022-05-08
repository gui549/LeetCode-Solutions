package Medium;

import java.util.Stack;

// better solution
class Solution {
    public boolean find132pattern(int[] nums) {
        int n = nums.length, top = n, second = Integer.MIN_VALUE;

        for (int i = n - 1; i >= 0; i--) {
            if (nums[i] < second) return true;
            while (top < n && nums[i] > nums[top]) second = nums[top++];
            nums[--top] = nums[i];
        }
        
        return false;
    }
}


// first soltuion
// class Solution {
//     public boolean find132pattern(int[] nums) {
//         int n = nums.length, second = Integer.MIN_VALUE;
//         Stack<Integer> stack = new Stack<>();
//         for (int i = n - 1; i >= 0; i--) {
//             if (nums[i] < second) return true;
//             while (!stack.isEmpty() && stack.peek() < nums[i]) {
//                 second = Math.max(second, stack.pop());
//             }
//             stack.add(nums[i]);
//         } 
        
//         return false;
//     }
// }

