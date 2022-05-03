package Medium;

// better solution
class Solution {
    public int findUnsortedSubarray(int[] nums) {
        int n = nums.length, start = -1, end = -2, min = nums[n - 1], max = nums[0];
        for (int i = 0; i < n; i++) {
            max = Math.max(max, nums[i]);
            min = Math.min(min, nums[n - 1 - i]);
            if (nums[i] < max) end = i;
            if (nums[n - 1 - i] > min) start = n - 1 - i;
        }
        return end - start + 1;
    }
}


// first solution
// class Solution {
//     public int findUnsortedSubarray(int[] nums) {
//         int start = -1, end = -2, maxValue = Integer.MIN_VALUE;
//         for (int i = 0; i < nums.length; i++) {
//             if (maxValue < nums[i]) {
//                 maxValue = nums[i];
//             } else if (maxValue > nums[i]) {
//                 end = i;
//                 if (start == -1) {
//                     for (start = 0; start < i; start++) {
//                         if (nums[start] > nums[i]) break;
//                     }
//                 } else { 
//                     for (; start > 0; start--) {
//                         if (nums[start - 1] <= nums[i]) break;
//                     }
//                 }
//             }
//         }
//         return end - start + 1;
//     }
// }
