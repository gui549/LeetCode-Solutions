package Medium;

class Solution {
    public void sortColors(int[] nums) {
        int lo = 0, hi = nums.length - 1;
        for (int i = 0; i <= hi;) {
            if (nums[i] == 0) {
                int tmp = nums[lo];
                nums[lo] = nums[i];
                nums[i] = tmp;
                lo++; i++;
            } else if (nums[i] == 2) {
                int tmp = nums[hi];
                nums[hi] = nums[i];
                nums[i] = tmp;
                hi--;
            } else {
                i++;
            }
        }
    }
}


// class Solution {
//     public void sortColors(int[] nums) {
//         int redEnd = -1, whiteEnd = -1;
//         for (int i = 0; i < nums.length; i++) {
//             if (nums[i] == 0) {
//                 int tmp = nums[++redEnd]; // 1
//                 if (redEnd == ++whiteEnd) {
//                     nums[redEnd] = nums[i];
//                     nums[i] = tmp;
//                 } else {
//                     int tmp2 = nums[whiteEnd]; // 0
//                     nums[redEnd] = nums[i]; // [0, 0]
//                     nums[whiteEnd] = tmp; // [0, 1]
//                     if (whiteEnd < i) nums[i] = tmp2; // 
//                 }
//             } else if (nums[i] == 1) {
//                 int tmp = nums[++whiteEnd];
//                 nums[whiteEnd] = nums[i];
//                 nums[i] = tmp;
//             }
//         }
//     }
// }

// class Solution {
//     public void sortColors(int[] nums) {
//         int whiteFront = 0, blueFront = 0;
//         for (int i = 0; i < nums.length; i++) {
//             if (nums[i] == 0) {
//                 if (whiteFront == blueFront) {
//                     int tmp = nums[whiteFront];
//                     nums[whiteFront++] = nums[i];
//                     nums[i] = tmp;
//                     blueFront++;
//                 } else{
//                     int tmp1 = nums[whiteFront];
//                     nums[whiteFront++] = nums[i];
//                     int tmp2 = nums[blueFront];
//                     nums[blueFront++] = tmp1;
//                     nums[i] = tmp2;
//                 }
//             } else if (nums[i] == 1) {
//                 int tmp = nums[blueFront];
//                 nums[blueFront++] = nums[i];
//                 nums[i] = tmp;
//             }
//         }
//     }
// }

/**
 * [0, 2, 2, 1, 0, 2]
 */